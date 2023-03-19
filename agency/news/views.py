from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# переменные
menu = [{'title_menu': 'Главаня страница', 'url_name': '/'},
        {'title_menu': 'Недвижемость', 'url_name': '/'},  # добаить url и шаблон
        {'title_menu': 'Профиль', 'url_name': '/'},  # добаить url и шаблон
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


def enter(request):
    return render(request, 'news/enter.html')


# функции
def about(request):
    return render(request, 'news/about.html', {'title': 'О нас',
                                               'menu': menu})


def test(request):
    return HttpResponse('<h1> Test </h1>')


def get_year(request, now_year):
    if now_year > 2023:
        raise Http404()
    return HttpResponse(f'сейчас {now_year} год')


def myconfig(request, my_config):
    return HttpResponse(f'твой конфиг {my_config}')


def archive(request, year):
    return HttpResponse(f'сейчас {year} год')


def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибка')  # ообработка ошибки
