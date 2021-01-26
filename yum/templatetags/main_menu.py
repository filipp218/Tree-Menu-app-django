from django import template
from yum.models import MenuItem


register = template.Library()

def into_tree(parent, children_by_parent): #функция, которая берёт родителя и смотрит  есть ли у него дети, если есть она идёт в глубь и спрашивает у следующего сына.
    if parent in children_by_parent:
        parent.children = children_by_parent[parent]
        for m in children_by_parent[parent]:
            into_tree(m, children_by_parent)
    else:
        return parent

@register.inclusion_tag('yum/menu.html')
def main_tree(name):
    menu = MenuItem.objects.filter(name = name)
    children_by_parent = {}
    for m in menu:
        if m.parent not in children_by_parent:
            children_by_parent[m.parent] = [m]
        else:
            children_by_parent[m.parent].append(m)

    result = children_by_parent[None]
    for m in result:
        into_tree(m, children_by_parent)
    return {'menu': result}
    
    start_code = ['{% if item.children %}','<ul>','{% for child in item.children %}','<li> {{child}} </li>']
    end_code = ['{% endfor %}','</ul>']
