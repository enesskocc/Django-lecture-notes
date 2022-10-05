from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'user_example/index.html')


def special(request):
    return render(request, "user_example/special.html")


def register(request):
    form = UserCreationForm(request.POST or None) ## UserCreationForm hazir form. Kendimizin degil!
    # form = UserCreationForm() 14. satirdaki ile bu uc satir(14-15-16) ayni isi yapiyor.!
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login')

    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)