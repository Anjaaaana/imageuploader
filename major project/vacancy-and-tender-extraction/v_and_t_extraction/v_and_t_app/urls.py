from django.contrib import admin
from django.urls import path
from v_and_t_app import views
from . import views
urlpatterns = [
    path("",views.login,name='login'),
    path("login",views.index,name='index'),
    
]

