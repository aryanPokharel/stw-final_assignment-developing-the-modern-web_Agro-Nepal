from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from requests import get, post

# Create your views here.

def userlogin_view(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User()
        users = User.objects.all()

        user_username = user.username
        user_password = user.password

        if (user_username == username) and (user_password == password):
            return redirect('products/')


        else:
            messages.info(request, "Invalid Credentials!")
            return redirect('automobiles/')

    else:
        return render(request, 'loginuser.html')



def adduser_view(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/users/')

    context = {
        'form': form,
    }

    return render(request, 'registeruser.html', context)




