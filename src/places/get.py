import requests
import json
import time
from . import config
from .models import City, Place
from django.core import serializers


def get_places(city):
    try:
        obj = City.objects.get(name=city)
    except City.DoesNotExist:
        obj = None
    if not obj or obj.time < time.time()-10000 or obj.uses > 5:
        places = fetch_places(city)
        cash_places(places, city)
    use_city(city)
    return serializers.serialize("json", Place.objects.filter(city__name=city).order_by('?')[:config.PLACES_COUNT])


def cash_places(places, city):
    try:
        obj = City.objects.get(name=city)
        obj.delete()
    except City.DoesNotExist:
        pass
    ct = City(name=city, time=time.time())
    ct.save()
    Place.objects.bulk_create([Place(city=ct, name=p[0], categories=p[1],
                                     description=p[2], coordinates=p[3]) for p in places])


def use_city(city):
    ct = City.objects.get(name=city)
    ct.uses += 1
    ct.save()


def fetch_places(city):
    # returns list of places or error
    url = (f"https://search-maps.yandex.ru/v1/?text={city},Еда&"
           f"type=biz&results=500&lang=ru_RU&apikey={config.PLACES_API_KEY}")
    r = requests.get(url)
    # get places using Yandex API
    if r.status_code != 200: raise ValueError(r.text)  # error
    data = json.loads(r.text)["features"]
    if len(data) < config.PLACES_COUNT: raise ValueError('Places not found')  # places not found

    places = []
    for place in data:
        categories = " ".join([category['name'] for category in place['properties']['CompanyMetaData']['Categories']])
        # create string of categories
        coordinates = " ".join(map(str, place['geometry']['coordinates'][::-1]))
        places.append([place['properties']['name'], categories, place['properties']['description'], coordinates])
    return(places)
