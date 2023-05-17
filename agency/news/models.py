from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify


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

        return reverse('home', kwargs={'news_slug': self.slug})  # абслоютная ссылка


    class Meta:  # админка
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Категория новости'
        verbose_name_plural = 'Категории новостей'
        ordering = ['-name']  # обратное направление


class User(AbstractUser):
    Gender = (
        ('М', 'Мужчина'),
        ('Ж', 'Женщина'),
    )
    gender = models.CharField(max_length=1, verbose_name="Пол", choices=Gender, blank=True)
    phone = models.CharField(max_length=20, verbose_name="Телефон", unique=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', blank=True)
    birthday = models.DateTimeField(verbose_name='Дата рождения', blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', verbose_name='Аватарки', blank=True)
    description = models.TextField(verbose_name="О себе", blank=True)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'User_slug': self.slug})

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['last_name', 'first_name', 'username']


class Services(models.Model):
    name = models.CharField(max_length=50, verbose_name='Услуга', unique=True, )
    description = models.TextField(verbose_name='Описание', )
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('real_estate', kwargs={'services_slug': self.slug})

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Сategories_real_estate(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категории', unique=True, )
    description = models.TextField(verbose_name='Описание', )
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse('real_estate', kwargs={'categories_real_estate': self.slug})

    class Meta:
        verbose_name = 'Категория помещений'
        verbose_name_plural = 'Категории помещений'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Город')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('real_estate', kwargs={'city': self.slug})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'





class Real_estate(models.Model):
    user = models.ForeignKey('User', on_delete=models.PROTECT, null=True)
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    address = models.CharField(max_length=50, verbose_name='Адрес')

    category_name = models.ForeignKey('Сategories_real_estate', on_delete=models.CASCADE, null=True,
                                      verbose_name='Категория')
    services = models.ForeignKey('Services', on_delete=models.PROTECT, null=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    aray = models.FloatField(verbose_name='площадь', )
    price = models.IntegerField( verbose_name='цена')
    description = models.TextField(verbose_name='Описание', blank=True)
    first_photo = models.ImageField(upload_to='real_estate_first/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL', )



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{str(self.city)}-{str(self.street)}-{str(self.address)}', lowercase=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('real_estate', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'
        ordering = ['city', 'street']

class Real_estateImages(models.Model):
    real_estate = models.ForeignKey('Real_estate', verbose_name='Помещение ', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='real_estate/%Y/%m/%d/', verbose_name='Изображение', blank=True)

    class Meta:
        ordering = ['real_estate']
        verbose_name = 'Фотография '
        verbose_name_plural = 'Фотографии'