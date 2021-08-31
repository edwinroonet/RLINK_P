from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def NowDate():
  """
    Returns the value datetime now.
  """
  date = datetime.now().strftime("%Y-%m-%d")
  return date
