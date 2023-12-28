# weather_app
Weather web app with django, it's connected to openweather api 

this project got two function an index and second 
index is just to see the current weather 
second to see a daily forcast 

* you need to get an api key from openweather site 

and for working a daily forcast you need to have 16 day subscription in openweather

### How to Run

1. First clone the project and cd to project directory

```commandline
git clone <url of the project>
cd Password-generator
```

2. Make a python virtual env

```commandline
python3 -m venv <name of your venv>
```

3. Activate your venv

#### on linux

```commandline
source ./venv/bin/activate
```

#### on windows

```commandline
venv/bin/activate
```

4. Install the python packages

```commandline
pip install -r requirements.txt
```

5. Run the file

```commandline
python manage.py runserver
```