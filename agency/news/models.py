from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контен')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата редактирования ')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фотография')
    ispublic = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})  # абслоютная ссылка

    class Meta:  # админка
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    description = models.TextField( verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name'] # обратное направление

class User(AbstractUser):
    Gender = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    gender = models.CharField(max_length=1, verbose_name="Пол", choices=Gender, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', blank=True)
    birthday = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', verbose_name='Аватарки',  blank=True)
    def get_absolute_url(self):
        return reverse('profile', kwargs={'User_slug': self.slug})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


# class Real_estate(models.Model):
#     user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
#     city = models.CharField(max_length=50, verbose_name='Город')
#     street = models.CharField(max_length=50, verbose_name='Улица')
#     address = models.CharField(max_length=50, verbose_name='Адрес')






