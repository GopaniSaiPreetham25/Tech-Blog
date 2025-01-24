from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('insert/',insert,name='insert'),
    path('viewdata/',viewdata,name='viewdata'),
    path('home/',home,name='home'),
]