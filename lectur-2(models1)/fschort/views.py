from django.shortcuts import render
from django.http import HttpResponse

def homeview(request):
    # databese'den(modelsden) veriyi burda cekiyoruz.
    return HttpResponse("Welcome backend")

# Create your views here.
