from django import forms
from .models import *


# формы
class Add_Real_estateForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label='Никнейм',)
    city = forms.ModelChoiceField(queryset=City.objects.all(), label='Город', empty_label='Город не выбран', )
    street = forms.CharField(max_length=50, label='Улица', widget=forms.TextInput(attrs={'class': 'form-add-real-estate-label'}))
    address = forms.CharField(max_length=50, label='Адрес', widget=forms.TextInput(attrs={'class': 'form-add-real-estate-label'}))
    category_name = forms.ModelChoiceField(queryset=Сategories_real_estate.objects.all(), label='Категория', empty_label='Категория не выбрана', )
    services = forms.ModelChoiceField(queryset=Services.objects.all(), label='Продать / Сдать в аренду', empty_label='Услуга не выбрана', )
    aray = forms.FloatField(label='Площадь', widget=forms.TextInput(attrs={'class': 'form-add-real-estate-label'}))
    price = forms.FloatField(label='Цена', widget=forms.TextInput(attrs={'class': 'form-add-real-estate-label'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10, 'class': 'form-add-real-estate-description'}) , label='Описание', required=False, )

