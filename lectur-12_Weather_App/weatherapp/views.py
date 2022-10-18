from django.shortcuts import render, get_object_or_404, redirect
from decouple import config
import requests
from pprint import pprint
from .models import City
from django.contrib import messages


def home(request):
    api_key = config('api_key')
    user_city = request.GET.get('city')
    if user_city:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={user_city}&appid={api_key}&units=metric'
        r = requests.get(url)
        if r.ok:  # r.status_code == 200
            content = r.json()
            r_city = content.get('name')
            if City.objects.filter(city=r_city):
                messages.warning(request, 'City already exists.')
            else:
                City.objects.create(city=r_city)
                messages.success(request, 'City created.')
        else:
            messages.error(request, 'City does not exists.')
        return redirect('home')

        # city = 'İstanbul'
    cities = City.objects.all()  # ['İstanbul', 'Berlin', 'Ankara']
    city_data = []
    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        r = requests.get(url)
        content = r.json()
        data = {
            'city': city,
            'temp': content.get('main').get('temp'),
            'description': content.get('weather')[0].get('description'),
            'icon': content.get('weather')[0].get('icon')
        }
        city_data.append(data)

    context = {
        'city_data': city_data
    }

    return render(request, 'weatherapp/home.html', context)


def delete(request, id):
    city = get_object_or_404(City, id=id)
    city.delete()
    messages.success(request, 'City deleted.')
    return redirect('home')
