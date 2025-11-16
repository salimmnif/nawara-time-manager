"""
Template tags personnalisés pour l'application tasks.
"""
from django import template

register = template.Library()


@register.filter
def get_item(dictionary, key):
    """
    Permet d'accéder à un élément d'un dictionnaire via une clé variable dans un template.
    Usage: {{ dictionary|get_item:key }}
    """
    if dictionary is None:
        return None
    return dictionary.get(key)


@register.filter
def mul(value, arg):
    """
    Multiplie la valeur par l'argument.
    Usage: {{ value|mul:arg }}
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0


@register.filter
def div(value, arg):
    """
    Divise la valeur par l'argument.
    Usage: {{ value|div:arg }}
    """
    try:
        return float(value) / float(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0
