# medium-tiny-clone


# Setup

First thing, cloning repository.
```
$ git clone blabla
$ cd medium-clone
```

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

### Via docker
```sh
$ docker-compose up -d --build
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py createsuperuser
```

Visit 127.0.0.1:8000 in your browser.
