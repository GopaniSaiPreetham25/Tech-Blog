from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('insert/',insert,name='insert'),
    path('viewdata/',viewdata,name='viewdata'),
    path('update/<int:id>',update,name='update'),
    path('delete/<int:id>',delete,name='delete'),
    path('home/',home,name='home'),
<<<<<<< HEAD
    path('Createaccount/',Createaccount,name='Createaccount'),
=======
    path('login/',login,name='login'),
>>>>>>> dab32d58bfdcd6577f8af91f9c0800bf234e7fd2
]