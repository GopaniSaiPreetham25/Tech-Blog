from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns=[
    path('',home,name='home'),
    path('blog/',blog,name='blog'),
    path('main/',main,name='main'),
    # path('update/<int:id>',update,name='update'),
    # path('delete/<int:id>',delete,name='delete'),
    path('createacc/',createacc,name='createacc'),
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('about/',about,name='about'),
    path('blog/<int:post_id>/',post_detail,name='post_detail'),
]
