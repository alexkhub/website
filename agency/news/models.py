from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    ispublic = models.BooleanField(default=True)

def __str__ (self):
    return self.title

def get_absolute_url(self):
    return reverse('post', kwargs={'post_id': self.pk}) #абслоютная ссылка