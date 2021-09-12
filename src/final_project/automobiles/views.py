from django.shortcuts import render, redirect
from .forms import AutomobileForm
from .models import Automobile


# Create your views here.

def automobile_view(request):
    automobile = Automobile()
    automobiles = Automobile.objects.all()

    context = {
        'automobiles': automobiles,
    }

    return render(request, 'automobile.html', context)


def postautomobile_view(request):
    form = AutomobileForm()

    if request.method == 'POST':
        form = AutomobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('automobile.html')

    context = {
        'form': form
    }

    return render(request, 'postautomobile.html', context)
