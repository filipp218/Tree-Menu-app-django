from django import template
from yum.models import menu_item


register = template.Library()

@register.inclusion_tag('yum/base.html')
def main_tree():
        menu = menu_item.objects.filter(name = 'header')
        return {'menu': menu}
