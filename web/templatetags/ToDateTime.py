from datetime import datetime

from django import template

register = template.Library()

@register.filter(name='ToDateTime')
def ToDateTime(value):
  """
    Returns the date_string to type datetime.
  """
  if isinstance(value, str):
      date = datetime.strptime(value, "%Y-%m-%d")
  return date
