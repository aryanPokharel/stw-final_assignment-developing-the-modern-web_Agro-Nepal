from django.shortcuts import render, redirect
from .forms import RemarkForm
from .models import Remark
import http


# Create your views here.

def remarkpage_view(request):
    form = RemarkForm()

    if request.method == 'POST':
        form = RemarkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/remarks/')

    context = {
        'form': form
    }

    return render(request, 'remarks.html', context)
