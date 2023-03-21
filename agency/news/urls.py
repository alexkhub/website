from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('real_estate/', real_estate, name='real_estate'),
    path('about/', about, name='about'),
    path('profile/', profile, name='profile'),
    path('enter/', enter, name='enter'),
    path('post/<int:post_id>/', show_post, name='post'),
    path('category/<int:category_id>/', show_category, name='category')

]