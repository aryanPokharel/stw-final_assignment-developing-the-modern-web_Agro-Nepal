from django.contrib import admin
from django.urls import path, include
from .views import feedbackpage_view


urlpatterns = [
    path('', feedbackpage_view),
]
