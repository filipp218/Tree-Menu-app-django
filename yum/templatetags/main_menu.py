from django import template
from yum.models import MenuItem


register = template.Library()

def into_tree(parent, children_by_parent,code): #функция, которая берёт родителя и смотрит  есть ли у него дети, если есть она идёт в глубь и спрашивает у следующего сына.
    if parent in children_by_parent:
        code.append('<ul>')
        for m in children_by_parent[parent]:
            code.append('<li>')
            code.append(m.title)
            into_tree(m, children_by_parent, code)
            code.append('</li>')
        code.append('</ul>')
    else:
        return


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
    code = []
    code.append('<ul>')
    for m in result:
        code.append('<li>')
        code.append(m.title)
        into_tree(m, children_by_parent, code)
        code.append('</li>')
    code.append('</ul>')
    p = {'a':code}
    return {'menu': p}
