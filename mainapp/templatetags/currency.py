from django import template

register = template.library()

@register.filter(name='rubles')
def format_currency(string_value):
    return f"{string_value} rub."