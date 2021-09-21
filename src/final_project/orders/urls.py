from django.contrib import admin
from django.urls import path, include
from .views import order_view

urlpatterns = [
    path('', order_view),
]