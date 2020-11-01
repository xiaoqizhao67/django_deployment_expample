from django import template

register = template.Library()

@register.filter
def func(value,arg):
    """
    this cuts out all values of "arg" from the string
    """
    return value.replace(arg,'')

#register.filter('cut',cut) ==>1st "cut" is string name, 2nd is cut function
