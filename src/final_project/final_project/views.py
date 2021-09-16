from django.shortcuts import render, redirect
from products.models import Product
from automobiles.models import Automobile

def allsaleitems_view(request):
    products = Product()
    automobiles = Automobile()
    context = {
        'products' : products,
        'automobiles' : automobiles,
    }

    return render(request, 'allsaleitems.html', context)

