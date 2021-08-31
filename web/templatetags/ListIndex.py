from django import template

register = template.Library()

@register.simple_tag
def ListIndex(list, value):
  """
    Returns the value index of list.
  """
  return list.index(value)
