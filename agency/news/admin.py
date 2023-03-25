from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', 'ispublic')  # отображаются в админке
    list_display_links = ('id', 'title')  # перехож при нажатии
    search_fields = ('title', 'content')  # поиск
    list_editable = ('ispublic',)  # возможность уредактирования
    list_filter = ('ispublic', 'created_at')  # фильтр


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
