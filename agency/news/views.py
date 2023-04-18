from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotFound, HttpResponseNotFound, Http404
from .models import *
from .forms import *
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
               'category_selected': 0,
               }
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


#работа с формой
def add_real_estate(request):
    if request.method == 'POST':
        form = Add_Real_estateForm(request.POST)
        if form.is_valid():
            try:
                Real_estate.objects.create(**form.cleaned_data)
                return redirect('real_estate')
            except:
                form.add_error(None, 'Ошибка добавления ')
    else:
        form = Add_Real_estateForm()


    context = {
        'title': 'Разместить на сайте',
        'menu': menu,
        'form': form,
                }
    return render(request, 'news/add_real_estate.html', context=context)

def show_real_estate(request):
    return render(request, 'news/show_real_estate.html')


# функции


def PageNotFound(request, exception):
    return HttpResponseNotFound('Ошибка')  # ообработка ошибки





def show_post(request, post_slug):
    post = get_object_or_404(News, slug=post_slug)

    context = {'title': 'Пост',

               'post': post,
               'title_news' : post.title,
               'content' : post.content,
               'created_at': post.created_at,
               'category_selected': post.category, }
    return render(request, 'news/post.html', context=context)


def show_category(request, category_slug):
    category = Category.objects.all()
    posts = News.objects.filter(slug=category_slug)

    context = {'title': 'Главная страница',
               'menu': menu,
               'posts': posts,
               'category': category,
               'category_selected': 0, }
    return render(request, 'news/index.html', context=context)
