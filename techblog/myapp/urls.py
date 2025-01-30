# # from django.urls import path
# # from .views import *

# # app_name='myapp'

# # urlpatterns=[
# #     path('',home,name='home'),
# #     path('blog/',blog,name='blog'),
# #     path('main/',main,name='main'),
# #     # path('update/<int:id>',update,name='update'),
# #     # path('delete/<int:id>',delete,name='delete'),
# #     path('createacc/',createacc,name='createacc'),
# #     path('home/',home,name='home'),
# #     path('login/',login,name='login'),
# # ]


# from django.urls import path
# from .views import *

# app_name = 'myapp'

# urlpatterns = [
#     path('', home, name='home'),
#     path('blog/', blog, name='blog'),
#     path('main/', main, name='main'),
#     path('createacc/', createacc, name='createacc'),
#     path('home/', home, name='home'),
#     path('login/', login, name='login'),
#     path('blog/<int:post_id>/', post_detail, name='post_detail'),
# ]

from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),  # Keeping one home URL
    path('login/', login, name='login'),
    path('createacc/', createacc, name='createacc'),

    path('blog/', blog, name='blog'),
    path('main/', main, name='main'),
    path('blog/<int:post_id>/', post_detail, name='post_detail'),  # Detail page for posts

    # Uncommented and fixed update & delete paths
    path('update/<int:id>/', update, name='update'),
    path('delete/<int:id>/', delete, name='delete'),
]
