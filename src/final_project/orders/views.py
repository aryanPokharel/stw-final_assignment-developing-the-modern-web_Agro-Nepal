from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.

def order_view(request):
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/products/')

    context = {
        'form': form
    }

    return render(request, 'orderform.html', context)