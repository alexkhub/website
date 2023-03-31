from django.db import models
from django.urls import reverse


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
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-name'] # обратное направление
