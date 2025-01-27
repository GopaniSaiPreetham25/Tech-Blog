from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('insert/',insert,name='insert'),
    path('main/',main,name='main'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('',home,name='home'),
    path('createacc/',createacc,name='createacc'),
    path('home/',home,name='home'),
    path('login/',login,name='login'),
    path('blog/',blog,name='blog'),
]