from django import template

register = template.Library()

@register.filter(name='blockpage')
def blockpage(value):
    page = int((value - 1) / 10) * 10 + 1
    return page
