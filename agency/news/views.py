from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request ):
    return render(request, 'news/index.html')


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
