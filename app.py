import json
import re
from random import sample
import requests
from flask import Flask, render_template, redirect, url_for, request
import config


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        return redirect(url_for('city', city=request.form["city"]))
    else:
        return render_template('index.html', config=config)


@app.route("/city/<string:city>")
def city(city):
    if not re.match("^[A-Za-zА-ЯёЁа-я- ]*$", city):  # check if city name is valid
        return render_template('index.html', alert_text="Wrong city name", config=config)  # if not - display error
    places = get_places(city)
    if not places or len(places) == 1:
        return render_template('index.html', alert_text=places[0], config=config)  # if error
    return render_template('places.html', places=places, city=city, config=config)


def get_places(city):
    # returns list of places or error
    url = (f"https://search-maps.yandex.ru/v1/?text={city},Еда&"
           f"type=biz&results=500&lang=ru_RU&apikey={config.PLACES_API_KEY}")
    r = requests.get(url)
    # get places using Yandex API
    if r.status_code != 200: return [r.text]  # error
    data = json.loads(r.text)
    if len(data["features"]) < config.PLACES_COUNT: return ['Places not found']  # places not found
    json_places = sample(data["features"], k=config.PLACES_COUNT)

    places = []
    for place in json_places:
        categories = " ".join([category['name'] for category in place['properties']['CompanyMetaData']['Categories']])
        # create string of categories
        coordinates = place['geometry']['coordinates'][::-1]
        places.append([place['properties']['name'], categories, place['properties']['description'], coordinates])
    return(places)


app.run()
