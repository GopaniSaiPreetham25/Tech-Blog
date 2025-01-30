<<<<<<< HEAD

=======
>>>>>>> 3aa15211ea1d3879558ea68e4410940506259515
from django.urls import path
from .views import *

app_name = 'myapp'

<<<<<<< HEAD
urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),  # Keeping one home URL
    path('login/', login, name='login'),
    path('createacc/', createacc, name='createacc'),
    path('blog/', blog, name='blog'),
    path('main/', main, name='main'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'), 
    path('about/',about,name='about')# Detail page for posts

=======
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
>>>>>>> 3aa15211ea1d3879558ea68e4410940506259515
]
