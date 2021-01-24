from django import template
from yum.models import MenuItem


register = template.Library()

@register.inclusion_tag('yum/menu.html')
def main_tree():
    menu = MenuItem.objects.all()
    return {'menu': menu}
