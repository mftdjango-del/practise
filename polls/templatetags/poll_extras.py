from django import template

register = template.Library()


@register.filter(name="seperator")
def seperator_digest(value):
    return "{:,}".format(int(value))


