import re
from . import city, places, config
from django.shortcuts import render


def home_view(request):
    print(request)
    return render(request, 'index.html', {'config': config})


def city_view(request):
    if request.method == 'GET':
        city_name = request.GET.get('s')
        if city_name and re.fullmatch(r"[A-Za-zА-ЯёЁа-я- ]*", city_name):
            try:
                ct = city.get(city_name)
                pl = list(places.get(ct).order_by('?').values()[:config.PLACES_COUNT])
            except ValueError as e:
                return render(request, 'index.html', {'alert_text': str(e), 'config': config})
            return render(request, 'places.html', {'city': city_name, 'places': pl, 'config': config})
        else:
            return render(request, 'index.html', {'alert_text': "Wrong city name", 'config': config})
