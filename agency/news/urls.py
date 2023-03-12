from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('test/', test),
    path('years/<int:now_year>/', get_year),
    path('config/<str:my_config>/', myconfig),
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)
]