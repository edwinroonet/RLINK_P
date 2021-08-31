from datetime import timedelta

from django import template

register = template.Library()

@register.filter(name='AddDays')
def AddDays(Date, value):
    """
        Returns the value add days.
      """
    return Date + timedelta(days=value)