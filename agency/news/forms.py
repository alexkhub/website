from django import forms
from .models import *


# формы
class Add_Real_estateForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    city = forms.ModelChoiceField(queryset=City.objects.all())
    street = forms.CharField(max_length=50, )
    address = forms.CharField(max_length=50, )
    category_name = forms.ModelChoiceField(queryset=Сategories_real_estate.objects.all())
    services = forms.ModelChoiceField(queryset=Services.objects.all())
    aray = forms.FloatField()
    price = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10}))
