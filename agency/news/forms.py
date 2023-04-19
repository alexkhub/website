from django import forms
from .models import *


# формы
class Add_Real_estateForm(forms.ModelForm):
    class Meta:
        model = Real_estate
        fields = '__all__'
