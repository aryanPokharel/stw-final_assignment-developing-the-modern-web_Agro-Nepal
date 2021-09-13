from django.contrib import admin
from django.urls import path, include
from .views import product_view, addproduct_view, updateproduct_view

urlpatterns = [
    path('product.html', product_view),
    path('addproduct.html', addproduct_view),
    path('updateproduct.html /<str:pk>/', updateproduct_view),


]