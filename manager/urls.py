from os import name
from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('login', views.login, name="login"),
    path('blog', views.blog, name="blog"),
    path('myaccount', views.myaccount, name="myaccount"),
]
