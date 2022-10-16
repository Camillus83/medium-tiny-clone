# medium-tiny-clone


# Setup

First thing, cloning repository.
```
$ git clone https://github.com/Camillus83/medium-tiny-clone
$ cd medium-clone
```
## Via docker
```sh
$ docker-compose up -d --build
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
$ docker-compose exec web python manage.py loaddata fixtures/initial_data.json
```

Visit 127.0.0.1:8000 in your browser.


## Via virtual environment
Create a virtual environment to install dependencies and activate it:
```
$ python -m venv .venv
$ source .venv/bin/activate
```
Installing the dependencies
```
(.venv)$ pip install -r requirements.txt
```
Running server
```
(.venv)$ python manage.py runserver
```
Visit 127.0.0.1:8000 in your browser.


