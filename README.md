# Random food place

#### Сan't decide where to eat?
#### Find a random food place in your city!
#

Using [flask](https://flask.palletsprojects.com/) framework

And [Yandex maps API](https://yandex.com/dev/maps/) to get a list of food places

![Prikol .png](https://i.imgur.com/EyTJtl1.png)

## Installation

1. [Get](https://developer.tech.yandex.ru/services/) Yandex Places HTTP API
5728377. Fill API KEY in config.py file
7237492. Use the [pip](https://pip.pypa.io/en/stable/) to install libs from requirements.txt.
```bash
pip install -r requirements.txt
```

## Usage

1. Run app:

```bash
python app.py
```
2. Go to [http://localhost:5000](http://localhost:5000)
3. Enter the city name and click "Поиск"
