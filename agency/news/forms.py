from django import forms
from .models import *


# формы
class Add_Real_estateForm(forms.ModelForm):
    class Meta:
        model = Real_estate
        fields = ['user', 'city', 'address', 'category_name', 'services', 'aray', 'price', ' description']
        widgets = {
            'description' : forms.Textarea(attrs={'cols': 60 , 'row': 10})
        }

