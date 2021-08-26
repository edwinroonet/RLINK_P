from django import template

register = template.Library()

@register.filter(name='Trim')
def trim(value):
  """
    Returns the value strip.
  """
  return value.strip()
