from django.contrib import admin
from django.urls import path, include
from .views import userlogin_view, adduser_view


print("urls running")
urlpatterns = [
    path('', userlogin_view),
    path('users/', userlogin_view),
    path('adduser/', adduser_view),

]
