from django.contrib import admin
from django.urls import path, include
from .views import insiderlogin_view, insiderregister_view

urlpatterns = [
    path('', insiderlogin_view),
    path('insiderregister/', insiderregister_view),
]