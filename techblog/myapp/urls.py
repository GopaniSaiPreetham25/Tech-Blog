from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('insert/',insert,name='insert'),
    path('viewdata/',viewdata,name='viewdata'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('',home,name='home'),
    path('Createaccount/',Createaccount,name='Createaccount'),
    path('home/',home,name='home'),
    path('createaccount/',createaccount,name='createaccount'),
    path('login/',login,name='login'),
]