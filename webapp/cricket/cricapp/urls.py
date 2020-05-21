from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.homepg, name='homepage'),
    path('user/', views.log, name='user'),
    path('about/', views.about, name='about'),
    path('userlogin/',views.auh, name='userlogin'),
    path('usercal/',views.cal, name='usercal'),
    path('tutorials/',views.tuto, name='tutorials'),
]