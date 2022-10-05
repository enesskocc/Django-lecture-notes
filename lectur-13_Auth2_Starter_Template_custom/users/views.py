from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Aferim ciktin')
    return redirect('home')

def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Hadi bakalim kayit oldun!')
        return redirect('home')

    context = {
    'form' : form
    }

    return render(request, 'users/register.html', context)

def user_login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        user = form.get_user()
        if user :
            login(request, user)
            messages.success(request, 'Looged in')
            return redirect('home')

    context = {
        'form' : form
    }

    return render(request, 'users/user_login.html', context)

