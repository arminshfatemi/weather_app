import datetime

from django.shortcuts import render
import requests
import urllib.request
import json


"""if want to just get current weather use function below """


# def index(request):
#    if request.method == "POST":
#        city = request.POST['city']
#        print(city)
#        src = urllib.request.urlopen(
#            f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=your key').read()
#
#        data_list = json.loads(src)
#        data_dict = {
#            'country_code': str(data_list['sys']['country']),
#            'coordinate': str(data_list['coord']['lon']) + ", " + str(data_list["coord"]["lat"]),
#            'temp': str(data_list['main']['temp']) + " °C",
#            'pressure': str(data_list['main']['pressure']),
#            'humidity': str(data_list['main']["humidity"]),
#            "main": str(data_list['weather'][0]['main']),
#            "description": str(data_list['weather'][0]['description']),
#            "icon": str(data_list['weather'][0]['icon']),
#        }
#
#        daily_src = urllib.request.urlopen(
#            f'http://api.openweathermap.org/data/2.5/forecast?q={city}&&units=metric&appid= your key').read()
#
#
#
#    else:
#        data_dict = {}
#
#    return render(request, 'main/index.html', data_dict)

def second(request):
    key = "your key"
    current_weather = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'
    forcast = 'http://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&units=metric&exclude=current,minutely,hourly,alerts&appid={}'

    if request.method == "POST":
        city = request.POST['city']
        print(city)
        weather_data_dict, week_forcast = current_forcast(request, current_weather, forcast, key, city )

        context = {
            'weather_data': weather_data_dict,
            'week_forcast': week_forcast,
        }

        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html')


def current_forcast(request, current_weather, forcast, key, city):
    current_response = urllib.request.urlopen(current_weather.format(city,key)).read()
    current_json = json.loads(current_response)
    lat = current_json['coord']['lat']
    lon = current_json['coord']['lon']
    forcast_response = urllib.request.urlopen(forcast.format(lat, lon, key)).read()
    forcast_json = json.loads(forcast_response)

    weather_data_dict = {
        'city': city,
        'temp': current_json['main']['temp'],
        'description': current_json['weather'][0]['description'],
        'icon': current_json['weather'][0]['icon'],
    }

    week_forcast = []
    for week_data in forcast_json['daily'][:5]:
        week_forcast.append({
            'day': datetime.datetime.fromtimestamp(week_data['dt']).strftime("%A"),
            'min_temp': week_data['temp']['min'],
            'max_temp': week_data['temp']['max'],
            'description': week_data['weather'][0]['description'],
            'icon': week_data['weather'][0]['icon'],
        })
    return weather_data_dict, week_forcast
