from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('regiter', views.regiter, name='regiter'),
    path('home', views.home, name='home'),
    path('user', views.user, name='user'),
    path('logindo', views.logindo, name='logindo'),
    path('loginout', views.loginout, name='loginout'),
    path('regiterdo', views.regiterdo, name='regiterdo'),
    path('regiterout', views.regiterout, name='regiterout'),
    path('host', views.host, name='host'),
    path('change', views.change, name='change'),
    path('changedo', views.changedo, name='changedo'),
    path('upload', views.upload, name='upload'),
    path('uploaddo', views.uploaddo, name='uploaddo'),
]