from django import template

register = template.Library()

@register.filter(name='Range')
def Range(value):
  """
    Returns the value make a range.
  """
  return range(value)
