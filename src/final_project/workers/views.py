from django.shortcuts import render, redirect
from .forms import WorkerForm
from .models import Worker


# Create your views here.

def join_worker(request):
    worker = Worker()
    workers = Worker.objects.all()

    context = {
        'workers': workers,
    }

    return render(request, 'farmer.html', context)


def joinform_view(request):
    form = WorkerForm()

    if request.method == 'POST':
        form = WorkerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmer.html')

    context = {'form': form}

    return render(request, 'joinform.html', context)


def updateworker_view(request, pk):

    worker = Worker.objects.get(id=pk)
    form = WorkerForm(instance=worker)

    context = {'form': form}

    return render(request, 'joinform.html', context)
