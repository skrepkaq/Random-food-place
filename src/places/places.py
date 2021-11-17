import json
import requests
from .models import Place
from . import config


def get(city):
    queryset = Place.objects.filter(city=city)
    if len(queryset) < 1:
        create(city)
    return Place.objects.filter(city=city)


def create(city):
    Place.objects.filter(city=city).delete()
    places = fetch_places(city.name)
    Place.objects.bulk_create([Place(city=city, name=p[0], categories=p[1],
                                     description=p[2], coordinates=p[3]) for p in places])


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
