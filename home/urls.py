from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('message/', views.MessageView.as_view(), name='message'),
]