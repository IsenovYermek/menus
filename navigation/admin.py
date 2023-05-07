from django.contrib import admin
from navigation.models import MenuItem
from navigation.forms import MenuItemAdminForm


# Определяем встроенный класс для редактирования объектов MenuItem в админской панели Djano.
class MenuItemInline(admin.TabularInline):
    model = MenuItem
    form = MenuItemAdminForm
    exclude = ('menu',)


# Определяем класс MenuItemAdmin для отображения объектов MenuItem в административной панели Django.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'menu', 'parent')
    list_filter = ('menu',)
    search_fields = ('title', 'url')
    form = MenuItemAdminForm
    inlines = [MenuItemInline]


admin.site.register(MenuItem, MenuItemAdmin)
