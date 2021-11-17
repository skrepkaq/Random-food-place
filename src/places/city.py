import time
from .models import City
from . import places


def get(city_name):
    queryset = City.objects.filter(name=city_name)
    if len(queryset) != 1:
        create(city_name)
    elif queryset[0].uses > 5 or queryset[0].time < time.time()-10000:
        update(queryset[0])
    city = City.objects.filter(name=city_name)[0]
    city.uses += 1
    city.save()
    return city


def create(city_name):
    print(f'deleted {city_name}')
    City.objects.filter(name=city_name).delete()
    City(name=city_name, time=time.time()).save()


def update(city):
    city.uses = 0
    city.time = time.time()
    city.save()
    places.create(city)
