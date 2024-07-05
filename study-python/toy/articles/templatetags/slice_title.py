from django import template

register = template.Library()


@register.filter()
def slicer(value, arg) -> str:
    if len(arg) > 35:
        value = arg[:36] + "..."
    return value
