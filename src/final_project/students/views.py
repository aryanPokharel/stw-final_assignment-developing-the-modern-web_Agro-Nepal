from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def showform(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'studentform.html', context)