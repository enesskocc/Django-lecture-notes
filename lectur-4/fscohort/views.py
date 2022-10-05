from cgitb import html
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {
        'company': 'clarusway',
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4]
    }
    return render(request, "fscohort/home.html", context)
