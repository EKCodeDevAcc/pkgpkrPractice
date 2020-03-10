from django.contrib import admin
#from django.urls import path
from django.conf.urls import url
#import repositories.views
from repositories import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', repositories.views.home, name='home'),
#     path('myrepositories/', repositories.views.my_repositories, name='my_repositories'),
#     path('myrepositories/(\d+)/', repositories.views.repository_detail, name='repository_detail'),
#     path('recommendations/', repositories.views.recommendations, name='recommendations'),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^myrepositories/', views.my_repositories, name='my_repositories'),
    url(r'^repository/(\d+)/', views.repository_detail, name='repository_detail'),
    url(r'^recommendations/', views.recommendations, name='recommendations'),
]
