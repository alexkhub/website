from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', 'ispublic')  # отображаются в админке
    list_display_links = ('id', 'title')  # перехож при нажатии
    search_fields = ('title', 'content')  # поиск
    list_editable = ('ispublic',)  # возможность редактирования
    list_filter = ('ispublic', 'created_at')  # фильтр
    prepopulated_fields = {"slug": ("title",)}  # заполнение поля slug


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_login', 'username', 'email', 'gender', 'phone', 'is_staff')
    list_display_links = ('id', 'last_login', 'username', 'email', 'phone',)
    prepopulated_fields = {"slug": ("username",)}
    search_fields = ('id', 'username', 'phone',)
    list_filter = ('is_staff',)
    list_editable = ('is_staff',)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    list_display_links = ('name',)
    list_editable = ('description',)
    prepopulated_fields = {"slug": ("name",)}


class Сategories_real_estateAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'description')
    list_display_links = ('category_name',)
    list_editable = ('description',)
    prepopulated_fields = {"slug": ("category_name",)}

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    prepopulated_fields = {"slug": ("name",)}



class Real_estateImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'real_estate')


#доделать админ класс real_estate
class Real_estateAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'address', 'status', 'aray', 'price')
    list_display_links = ('id', 'city', 'street', )
    list_filter = ('id', 'city', 'aray', 'price')
    list_editable = ('status',)
    prepopulated_fields = {'slug' : ('city', 'street', 'address')}


# подлючение к админке
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Сategories_real_estate, Сategories_real_estateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Real_estateImages, Real_estateImagesAdmin)
admin.site.register(Real_estate, Real_estateAdmin)
