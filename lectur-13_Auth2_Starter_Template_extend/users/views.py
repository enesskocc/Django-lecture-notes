from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from django.contrib import messages
from .forms import UserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def user_logout(request):
    logout(request)
    messages.success(request, 'Aferim ciktin')
    return redirect('home')

def register(request):
    form_user = UserForm()
    form_profile = UserProfileForm()

    if request.method == 'POST':
        form_user = UserForm(request.POST)
        form_profile = UserProfileForm(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            user = form_user.save()
            profile = form_profile.save(commit = False) ## objeye dönüstür, fakat database kaydetme! Profile User'i ekleyebilmek icin.
            profile.user = user
            profile.save()
            login(request, user)

            messages.success(request, 'Hadi bakalim kayit oldun!')
            return redirect('home')

    context = {
        'form_user' : form_user,
        'form_profile' : form_profile
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
