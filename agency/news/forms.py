from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


# формы
class Add_Real_estateForm(forms.ModelForm):
    class Meta:
        model = Real_estate
        fields = ['user', 'city', 'address', 'category_name', 'services', 'aray', 'price', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'row': 10})
        }


class Registration_CreationForm(UserCreationForm):
    # username = forms.CharField(label="Никнейм", widget=forms.TextInput())
    # first_name = forms.CharField(label="Имя", widget=forms.TextInput())
    # last_name = forms.CharField(label="Фамилия", widget=forms.TextInput())
    # password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput())
    # password2 = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput())
    # email = forms.EmailField(label='email', widget=forms.EmailInput())
    # gender = forms.ChoiceField(label='Пол',  choices=((1, 'Муж'), (2, 'Жен')), widget=forms.CheckboxInput())
    # birthday = forms.DateField(label="День рождения", widget=forms.DateInput())
    # avatar = forms.ImageField(label='Аватарка', widget=forms.FileInput())
    # phone = forms.CharField(label="Номер телефона", widget=forms.TextInput())
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'slug', 'gender',
                  'birthday', 'avatar', 'phone']


class Registration_ChangeForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'slug', 'gender',
                  'birthday', 'avatar', 'phone']
