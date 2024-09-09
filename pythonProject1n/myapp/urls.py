from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('',views.ListFunction, name='list'),
    path('edit/<str:pk>', views.EditFunction, name='edit'),
    path('delete/<str:pk>', views.DeleteFunction, name='delete'),
    path('create', views.CreateFunction, name='create')
    ]
