from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('real_estate/', real_estate, name='real_estate'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('enter/', enter, name='enter'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', show_category, name='category'),

]