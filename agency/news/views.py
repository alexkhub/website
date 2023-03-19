from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# переменные
menu = [{'title_menu': 'Главаня страница', 'url_name': 'home'},
        {'title_menu': 'Недвижемость', 'url_name': 'real_estate'},  # добаить url и шаблон
        {'title_menu': 'Профиль', 'url_name': 'profile'},  # добаить url и шаблон
        {'title_menu': 'О нас', 'url_name': 'about'},  # добаить url и шаблон
        {'title_menu': 'Войти', 'url_name': 'enter'},  # добаить url
        ]


# страницы
def index(request):
    posts = News.objects.all()
    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts}
    return render(request, 'news/index.html', context=context)


def real_estate(request):
    context = {'title': 'Недвижемость',
               'menu': menu}

    return render(request, 'news/real_estate.html', context=context)


def enter(request):
    return render(request, 'news/enter.html')


def about(request):
    context = {'title': 'О нас',
               'menu': menu}
    return render(request, 'news/about.html', context=context)


def profile(request):
    context = {
        'title': 'Профиль',
        'menu': menu}
    return render(request, 'news/profile.html', context=context)


# функции


def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибка')  # ообработка ошибки
