import re
from . import get, config
from django.shortcuts import render


def home_view(request):
    print(request)
    return render(request, 'index.html', {'config': config})


def city_view(request):
    if request.method == 'GET':
        city = request.GET.get('s')
        if city and re.fullmatch(r"[A-Za-zА-ЯёЁа-я- ]*", city):
            try:
                pl = get.get_places(city)
            except ValueError as e:
                return render(request, 'index.html', {'alert_text': str(e), 'config': config})
            return render(request, 'places.html', {'city': city, 'places': pl, 'config': config})
        else:
            return render(request, 'index.html', {'alert_text': "Wrong city name", 'config': config})
