# That __init__.py makes this directory (templatetags) a Python Module


from django import template

register = template.Library()

def cut(value, arg):
    return value.replace(arg,'')


register.filter('cut',cut) #KEEP THE NAME SAME!
