from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', 'ispublic')  # отображаются в админке
    list_display_links = ('id', 'title')  # перехож при нажатии
    search_fields = ('title', 'content')  # поиск
    list_editable = ('ispublic',)  # возможность уредактирования
    list_filter = ('ispublic', 'created_at')  # фильтр
    prepopulated_fields = {"slug": ("title",)} # заполнение поля slug

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name", )}

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', )

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)