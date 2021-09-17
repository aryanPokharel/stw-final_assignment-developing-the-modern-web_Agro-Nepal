from django.shortcuts import render, redirect
from products.models import Product
from automobiles.models import Automobile

def allsaleitems_view(request):
    product = Product()
    products = Product.objects.all()

    automobile = Automobile()
    automobiles = Automobile.objects.all()
    context = {
        'products' : products,
        'automobiles' : automobiles,
    }

    return render(request, 'allsaleitems.html', context)

def learn_view(request):
    return render(request, 'learn.html')