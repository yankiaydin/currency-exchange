from django.contrib import admin
from django.urls import path
from finance import views

urlpatterns = [
    path('', views.exchanger, name='exchanger'),
]
