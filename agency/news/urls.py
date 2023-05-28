from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('real_estate/', Real_Estate.as_view(), name='real_estate'),
    path('profile/', Profile.as_view(), name='profile'),
    path('login/', Login.as_view(), name='login'),
    path('registration/', Registration.as_view(), name='registration'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('add_real_estate/', Add_Real_Estate.as_view(), name='add_real_estate'),
    path('show_real_estate/<slug:real_estate_slug>/', Show_Real_Estate.as_view(), name='show_real_estate'),

]