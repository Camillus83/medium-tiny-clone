# medium-tiny-clone
![image](https://user-images.githubusercontent.com/87909623/203655793-7bd8fb1b-be39-4a69-8628-c3a18a6ef1c5.png)
![image](https://user-images.githubusercontent.com/87909623/203655879-4269be42-31dd-4650-83b6-077abbf03490.png)
![image](https://user-images.githubusercontent.com/87909623/203655950-c07eda47-70b4-4d3d-9d11-a2158b9233fb.png)

Simple blog/medium clone. Still have some things to do! Will update later.
Please do not load fixtures, it's from previous version.
Cheers!

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


