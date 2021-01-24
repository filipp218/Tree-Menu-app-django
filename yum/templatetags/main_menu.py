from django import template
from yum.models import menu_item


register = template.Library()

@register.filter
def main_tree():
        menu = menu_item.objects.filter(name = header)
        return menu
