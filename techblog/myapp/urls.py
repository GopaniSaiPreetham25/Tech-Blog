<<<<<<< HEAD

=======
>>>>>>> 3035bc642fcff0227c82426395ac30839a96201c
from django.urls import path
from .views import *

app_name = 'myapp'
<<<<<<< HEAD
=======

>>>>>>> 3035bc642fcff0227c82426395ac30839a96201c
urlpatterns = [
    path('', home, name='home'), 
    path('login/', login, name='login'),
    path('createacc/', createacc, name='createacc'),
    path('blog/', blog, name='blog'),
    path('main/', main, name='main'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'), 
<<<<<<< HEAD
    path('about/',about,name='about')
=======
    path('about/',about,name='about')# Detail page for posts
>>>>>>> 3035bc642fcff0227c82426395ac30839a96201c
]

