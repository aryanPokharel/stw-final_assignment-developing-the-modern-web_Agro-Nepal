from django.shortcuts import render, redirect
from .forms import WorkerForm

# Create your views here.

def join_worker(request):

    context = {}

    return render(request, 'farmer.html', context)

def joinform_view(request):
    form = WorkerForm()

    if request.method == 'GET':
        form = WorkerForm(request.GET)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}

    return render(request, 'joinform.html', context)

