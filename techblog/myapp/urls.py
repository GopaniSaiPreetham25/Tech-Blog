from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'), 
    path('login/', login, name='login'),
    path('createacc/', createacc, name='createacc'),
    path('blog/', blog, name='blog'),
    path('main/', main, name='main'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'), 
    path('about/',about,name='about')
]
