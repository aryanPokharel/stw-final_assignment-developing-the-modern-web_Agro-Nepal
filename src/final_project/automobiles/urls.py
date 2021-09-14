from django.contrib import admin
from django.urls import path, include
from .views import automobile_view, addautomobile_view


urlpatterns = [
    path('', automobile_view),
    path('addautomobile/', addautomobile_view)
]