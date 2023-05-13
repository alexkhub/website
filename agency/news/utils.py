from .models import  *


menu = [{'title_menu': 'Главнaя страница', 'url_name': 'home'},
        {'title_menu': 'Недвижимость', 'url_name': 'real_estate'},  # добаить url и шаблон
        {'title_menu': 'Профиль', 'url_name': 'profile'},  # добаить url и шаблон
        {'title_menu': 'Войти', 'url_name': 'enter'},  # добаить url
        ]



class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['menu'] = menu
        return context
