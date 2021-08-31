from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def AddCount(object, string, count):
    key = string + str(count)
    return object[key]
