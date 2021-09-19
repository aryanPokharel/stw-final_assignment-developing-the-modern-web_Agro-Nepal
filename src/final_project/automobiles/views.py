from django.shortcuts import render, redirect
from .forms import AutomobileForm
from .models import Automobile


# Create your views here.

def automobile_view(request):
    automobile = Automobile()
    automobiles = Automobile.objects.all()


    # hireprice = (5 * automobile.price) / 100

    context = {
        'automobiles': automobiles,
        # 'hireprice': hireprice,
    }

    return render(request, 'automobiles.html', context)


def addautomobile_view(request):
    form = AutomobileForm()

    if request.method == 'POST':
        form = AutomobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('automobiles.html')

    context = {
        'form': form
    }

    return render(request, 'postautomobile.html', context)
