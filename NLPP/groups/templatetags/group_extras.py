from django import template

def update_variable(value):
    data = value
    return data

register = template.Library()
register.filter('update_variable', update_variable)
