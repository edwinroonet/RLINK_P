from datetime import datetime

from django import template

register = template.Library()

@register.filter(name='ToString')
def ToString(Date, format):
    """
        Returns the value datetime to date_string.
      """
    return datetime.strftime(Date, format)