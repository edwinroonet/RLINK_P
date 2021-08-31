from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def strdaydate(date):
    day_count = str(date.weekday())
    if day_count == "6":
        return "Sun"
    elif day_count == "0":
        return "Mon"
    elif day_count == "1":
        return "Tue"
    elif day_count == "2":
        return "Wed"
    elif day_count == "3":
        return "Thu"
    elif day_count == "4":
        return "Fri"
    elif day_count == "5":
        return "Sat"
    else:
        return ""
