from django import template

register = template.Library()

@register.filter(name='InStr')
def InStr(value, word):
    """
        Returns the value find word.
      """
    return value.find(word)