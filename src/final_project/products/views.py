from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def product_view(request):
    product = Product()
    products =Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'product.html', context)

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


