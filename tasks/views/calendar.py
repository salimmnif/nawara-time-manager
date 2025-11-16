"""
Vues pour le calendrier et les vues temporelles.
"""
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta, date
import calendar
from collections import defaultdict
from ..models import Task


class CalendarView(LoginRequiredMixin, TemplateView):
    """Vue du calendrier mensuel."""
    
    template_name = 'tasks/calendar.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenir le mois et l'année demandés (ou le mois actuel)
        today = timezone.now().date()
        year = int(self.request.GET.get('year', today.year))
        month = int(self.request.GET.get('month', today.month))
        
        # Créer un objet calendrier
        cal = calendar.monthcalendar(year, month)
        
        # Récupérer toutes les tâches du mois pour l'utilisateur
        first_day = date(year, month, 1)
        if month == 12:
            last_day = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = date(year, month + 1, 1) - timedelta(days=1)
        
        tasks = Task.objects.filter(
            user=self.request.user,
            due_date__gte=first_day,
            due_date__lte=last_day
        )
        
        # Grouper les tâches par jour
        tasks_by_day = defaultdict(list)
        for task in tasks:
            tasks_by_day[task.due_date.day].append(task)
        
        # Mois précédent et suivant pour navigation
        prev_month = month - 1 if month > 1 else 12
        prev_year = year if month > 1 else year - 1
        next_month = month + 1 if month < 12 else 1
        next_year = year if month < 12 else year + 1
        
        context.update({
            'calendar': cal,
            'tasks_by_day': dict(tasks_by_day),
            'current_month': month,
            'current_year': year,
            'month_name': calendar.month_name[month],
            'prev_month': prev_month,
            'prev_year': prev_year,
            'next_month': next_month,
            'next_year': next_year,
            'today': today,
        })
        
        return context


class DayView(LoginRequiredMixin, ListView):
    """Vue des tâches d'un jour spécifique."""
    
    model = Task
    template_name = 'tasks/day_view.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        """Retourne les tâches du jour spécifié."""
        # Obtenir la date demandée (ou aujourd'hui)
        today = timezone.now().date()
        date_str = self.request.GET.get('date')
        
        if date_str:
            try:
                target_date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                target_date = today
        else:
            target_date = today
        
        self.target_date = target_date
        
        return Task.objects.filter(
            user=self.request.user,
            due_date=target_date
        ).order_by('priority', 'created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['target_date'] = self.target_date
        context['is_today'] = self.target_date == timezone.now().date()
        
        # Navigation jour précédent/suivant
        context['prev_date'] = self.target_date - timedelta(days=1)
        context['next_date'] = self.target_date + timedelta(days=1)
        
        return context


class WeekView(LoginRequiredMixin, TemplateView):
    """Vue hebdomadaire des tâches."""
    
    template_name = 'tasks/week_view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtenir la semaine demandée (ou la semaine actuelle)
        today = timezone.now().date()
        date_str = self.request.GET.get('date')
        
        if date_str:
            try:
                reference_date = timezone.datetime.strptime(date_str, '%Y-%m-%d').date()
            except ValueError:
                reference_date = today
        else:
            reference_date = today
        
        # Calculer le début de la semaine (lundi)
        week_start = reference_date - timedelta(days=reference_date.weekday())
        week_end = week_start + timedelta(days=6)
        
        # Récupérer les tâches de la semaine
        tasks = Task.objects.filter(
            user=self.request.user,
            due_date__gte=week_start,
            due_date__lte=week_end
        ).order_by('due_date', 'priority')
        
        # Grouper les tâches par jour
        days_of_week = []
        tasks_by_day = defaultdict(list)
        
        for task in tasks:
            tasks_by_day[task.due_date].append(task)
        
        # Créer une liste de jours avec leurs tâches
        for i in range(7):
            day = week_start + timedelta(days=i)
            days_of_week.append({
                'date': day,
                'day_name': calendar.day_name[day.weekday()],
                'tasks': tasks_by_day[day],
                'is_today': day == today,
            })
        
        # Navigation semaine précédente/suivante
        prev_week = week_start - timedelta(days=7)
        next_week = week_start + timedelta(days=7)
        
        context.update({
            'week_start': week_start,
            'week_end': week_end,
            'days_of_week': days_of_week,
            'prev_week': prev_week,
            'next_week': next_week,
            'is_current_week': week_start <= today <= week_end,
        })
        
        return context
