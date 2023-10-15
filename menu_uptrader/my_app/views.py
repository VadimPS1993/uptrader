from django.shortcuts import render, get_object_or_404
from .models import MenuItem

def draw_menu(request, menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).select_related('parent')
    return render(request, 'my_app/menu_template.html', {'menu_items': menu_items, 'title': 'Страница меню'})