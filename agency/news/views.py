from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseNotFound, Http404
from .models import *

# переменные
menu = [{'title_menu': 'Главнaя страница', 'url_name': 'home'},
        {'title_menu': 'Недвижимость', 'url_name': 'real_estate'},  # добаить url и шаблон
        {'title_menu': 'Профиль', 'url_name': 'profile'},  # добаить url и шаблон
        {'title_menu': 'О нас', 'url_name': 'about'},  # добаить url и шаблон
        {'title_menu': 'Войти', 'url_name': 'enter'},  # добаить url
        ]


# страницы
def index(request):
    category = Category.objects.all()
    posts = News.objects.all()
    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts,
               'category': category,
               'category_selected': 0, }
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


def regidtration(request):
    return render(request, 'news/registration.html')


# функции


def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибка')  # ообработка ошибки





def show_post(request, post_id):
    post = get_object_or_404(News, pk=post_id)

    context = {'title': 'Главная страница',

               'post': post,
               'title' : post.title,
               'photo' : post.photo,
               'category_selected': 1, }
    return render(request, 'news/post.html', context=context)


def show_category(request, category_id):
    category = Category.objects.all()
    posts = News.objects.filter(category_id=category_id)

    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts,
               'category': category,
               'category_selected': 0, }
    return render(request, 'news/index.html', context=context)
