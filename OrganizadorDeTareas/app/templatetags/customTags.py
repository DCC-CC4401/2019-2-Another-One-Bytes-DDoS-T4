from django import template
register = template.Library()


def update_variable(value,arg):

    value=arg
    return value

register.filter('update_variable', update_variable)