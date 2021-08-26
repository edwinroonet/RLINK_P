from datetime import datetime

from django import template

register = template.Library()

@register.simple_tag
def fn_weekday(date):
    day_count = str(date.weekday())
    if day_count == "6":
        return "일"
    elif day_count == "0":
        return "월"
    elif day_count == "1":
        return "화"
    elif day_count == "2":
        return "수"
    elif day_count == "3":
        return "목"
    elif day_count == "4":
        return "금"
    elif day_count == "5":
        return "토"
    else:
        return ""
