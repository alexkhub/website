from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponseNotFound, Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *
from .forms import *
from .utils import *


# страницы

class Home(DataMixin, ListView):
    """Основная страница """

    model = News
    template_name = 'news/index.html'

    context_object_name = 'posts'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()  # передаем переменные из DataMixin
        context['title'] = 'Главная страница'
        context['categorys'] = Category.objects.all()

        return dict(list(context.items()) + list(c_def.items()))  # объединение данных

    def get_queryset(self):
        # проверка на публиуацию
        return News.objects.filter(ispublic=True)


class ShowPost(DetailView):
    """Просмотр поста """
    model = News
    slug_url_kwarg = 'post_slug'
    template_name = 'news/post.html'
    context_object_name = 'post'


class Real_Estate(DataMixin, ListView):
    """Объявления на сайте """
    model = Real_estate
    paginate_by = 3
    template_name = 'news/real_estate.html'
    context_object_name = 'real_estates'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()  # передаем переменные из DataMixin
        context['title'] = 'Недвижемость'

        return dict(list(context.items()) + list(c_def.items()))  # объединение данных

    def get_queryset(self):
        # проверка на публиуацию
        return Real_estate.objects.filter(status=True)


class Show_Real_Estate(DataMixin, DetailView):
    """Просмотр объявления"""
    model = Real_estate
    template_name = 'news/show_real_estate.html'
    slug_url_kwarg = 'real_estate_slug'
    context_object_name = 'real_estate'


class Profile(LoginRequiredMixin, DataMixin, ListView):
    """Профиль"""
    model = User
    template_name = 'news/profile.html'

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()  # передаем переменные из DataMixin
        context['title'] = 'Профиль'
        return dict(list(context.items()) + list(c_def.items()))  # объединение данных


# работа с формой


class Add_Real_Estate(LoginRequiredMixin, DataMixin, CreateView):
    """Добавление объявления"""
    form_class = Add_Real_estateForm
    template_name = 'news/add_real_estate.html'
    success_url = reverse_lazy('real_estate')  # отправление пользователя по ссылке
    login_url = reverse_lazy('enter')  # перенаправляет пользователя на страницу входа

    def get_context_data(self, object_list=None, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()  # передаем переменные из DataMixin
        context['title'] = 'Разместить на сайте '

        return dict(list(context.items()) + list(c_def.items()))  # объединени


class Registration(CreateView):
    """Регистрация"""
    form_class = Registration_CreationForm
    template_name = 'news/registration.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(LoginView):
    """Авторизация"""
    form_class = LoginForm
    template_name = 'news/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class Contact_Help(FormView):
    """Служба поддержки """
    form_class = Contact_Help_Form
    template_name = 'news/contact_help.html'
    success_url = reverse_lazy('home')


def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибка')  # ообработка ошибки


def logout_user(request):
    logout(request)
    return redirect('home')
