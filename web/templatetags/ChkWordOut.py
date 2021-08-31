from django import template

register = template.Library()

@register.simple_tag
def ChkWordOut(CheckValue):
    CheckValue = CheckValue.replace("&quot;", "\"\"")
    CheckValue = CheckValue.replace("<br>", "\r\n" )
    return CheckValue