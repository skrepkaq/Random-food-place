# Random food place

#### Сan't decide where to eat?
#### Find a random food place in your city!
#

Using [Django](https://www.djangoproject.com/) framework

[Yandex maps API](https://yandex.com/dev/maps/) to get a list of food places and show them on the map

![Prikol .png](https://i.imgur.com/cCU2917.png)

## Installation

1. [Get](https://developer.tech.yandex.ru/services/) Yandex "Places HTTP API" and "JS and Geocoder API"
2. Create and activate [venv](https://docs.python.org/3/library/venv.html)
5728377. Fill API KEYS in src/places/config.py file
7237492. Use the [pip](https://pip.pypa.io/en/stable/) to install libs from requirements.txt.
```bash
pip install -r requirements.txt
```
5. Migrate DB using manage.py file in src directory
```bash
python manage.py makemigrations
python manage.py migrate
```

## Usage

1. Run server:

```bash
python manage.py runserver
```
2. Go to [http://localhost:8000](http://localhost:8000)
3. Enter the city name and click "Поиск"
