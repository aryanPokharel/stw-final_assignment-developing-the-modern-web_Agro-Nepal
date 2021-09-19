from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from requests import get, post
from django.contrib.auth.decorators import login_required
from users.auth import unauthenticated_user, admin_only, user_only

# Create your views here.

@unauthenticated_user
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
        return render(request, 'insiderlogin.html')



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

    return render(request, 'insiderregister.html', context)

@login_required
def logout_user(request):
    logout(request)
    return redirect('/users/')


