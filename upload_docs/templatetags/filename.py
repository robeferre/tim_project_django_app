from django import template
register = template.Library()

@register.filter
def filename(value):
    array=value.rsplit('/')
    tam=len(array)
    file_name=array[tam-1]
    return file_name
