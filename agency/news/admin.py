from django.contrib import admin
from .models import *

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at') #отображаются в админке
    list_display_links = ('id', 'title') # перехож при нажатии
    search_fields = ('title', 'content') # поиск

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)