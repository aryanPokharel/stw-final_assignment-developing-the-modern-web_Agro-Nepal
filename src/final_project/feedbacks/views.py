from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
import http


# Create your views here.

def feedbackpage_view(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FeedbackForm()

    context = {
        'form': form
    }

    return render(request, 'feedbacks.html', context)


