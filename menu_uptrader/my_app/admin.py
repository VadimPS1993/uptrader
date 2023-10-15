from django.contrib import admin
from .models import *

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'named_url', 'parent')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(MenuItem, MenuItemAdmin)


