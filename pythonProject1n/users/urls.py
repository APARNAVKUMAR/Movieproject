from django.urls import path
from users import views

urlpatterns = [
    path('add', views.addUser, name='add'),
    path('login', views.LoginFunction, name='login'),
    path('logout', views.LogOut, name='logout'),
]