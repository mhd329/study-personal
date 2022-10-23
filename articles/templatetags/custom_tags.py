from django import template

register = template.Library()


# 13글자 까지만 표시하고 뒤는 ...
@register.filter()
def slicer(value, arg: str):
    if len(arg) > 12:
        value = arg[:13] + "..."
    return value


# 7글자 까지만 표시하고 뒤는 ...
@register.filter()
def sub_slicer(value, arg: str):
    if len(arg) > 7:
        value = arg[:7] + "..."
    return value


# 9글자 까지만 표시하고 뒤는 ...
@register.filter()
def mini_slicer(value, arg: str):
    if len(arg) > 8:
        value = arg[:9] + "..."
    return value


@register.filter()
def color_changer(value, arg: int):
    color_list = (
        "",
        "text-danger fw-bolder",
        "text warning fw-bolder",
        "text-warning",
        "text-secondary",
        "text-white",
    )
    i = (25 - arg) // 5
    if arg > 20:
        value = "text-danger fw-bolder"
        return value
    else:
        value = color_list[i]
        return value


@register.filter()
def star_range(count=10):
    return range(count)
