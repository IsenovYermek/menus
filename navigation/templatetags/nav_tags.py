from navigation.models import MenuItem
from django.template import Library
register = Library()


# Определение шаблонного тега Django для рисования меню на базе модели MenuItem.
@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    # Получение объекта запроса из контекста.
    request_path = context['request'].path
    menu_items = MenuItem.objects.filter(menu=menu_name)
    # Создание строки HTML-разметки для меню.
    menu_html = '<ul class="menu">'
    for item in menu_items:
        is_active = False
        if request_path.startswith(item.url):
            is_active = True

        menu_html += '<li class="menu-item %s">' % ('active' if is_active else '')
        menu_html += '<a href="%s">%s</a>' % (item.url, item.title)

        if item.children.all():
            menu_html += get_submenu(item.children.all(), request_path)

        menu_html += '</li>'
    menu_html += '</ul>'

    return menu_html


def get_submenu(children, request_path):
    menu_html = '<ul class="submenu">'
    for child in children:
        is_active = False
        if request_path.startswith(child.url):
            is_active = True

        submenu_html = '<li class="%s">' % ('active' if is_active else '')
        submenu_html += '<a href="%s">%s</a>' % (child.url, child.title)

        if child.children.all():
            submenu_html += get_submenu(child.children.all(), request_path)

        submenu_html += '</li>'
        menu_html += submenu_html
    menu_html += '</ul>'

    return menu_html
