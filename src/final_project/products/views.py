from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
def product_view(request):
    product = Product()
    products =Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product.html', context)

@login_required
def addproduct_view(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product.html')

    context = {
        'form': form
    }

    return render(request, 'addproduct.html', context)

def updateproduct_view(request, pk):
    form = ProductForm()
    context = {
        'form': form
    }

    return render(request, 'updateproduct.html', context)

def registeruser_view(request):
    context={}
    return render(request, 'registeruser.html', context)



