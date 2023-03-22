from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ispublic = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__ (self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk}) #абслоютная ссылка

    class Meta:
        verbose_name= 'Новость'
        verbose_name_plural = 'Новости'

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField()


    def __str__ (self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})