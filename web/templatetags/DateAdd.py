from datetime import timedelta

from django import template

register = template.Library()

@register.simple_tag
def DateAdd(Interval, Number, Date):
    if Interval == "d":
        Date + timedelta(days=Number)
    return Date.strftime("%Y-%m-%d")