from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('real_estate/', real_estate, name='real_estate'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('enter/', enter, name='enter'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('<slug:category_slug>/', Home.as_view(), name='home_category'),
    path('add_real_estate/', add_real_estate, name='add_real_estate'),
    path('show_real_estate/', show_real_estate, name='show_real_estate'),

]