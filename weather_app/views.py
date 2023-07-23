from django.shortcuts import render

import urllib.request
import json

def index(request):
    if request.method == "POST":
        city = request.POST['city']
        print(city)
        src = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+ city + "&units=metric&appid=53826a6a139e1f9fc0a410f3a0a0badd").read()

        data_list = json.loads(src)
        data_dict = {
            'country_code': str(data_list['sys']['country']),
            'coordinate': str(data_list['coord']['lon']) + ", " + str(data_list["coord"]["lat"]),
            'temp': str(data_list['main']['temp']) + " °C",
            'pressure': str(data_list['main']['pressure']),
            'humidity': str(data_list['main']["humidity"]),
            "main": str(data_list['weather'][0]['main']),
            "description": str(data_list['weather'][0]['description']),

            # "icon": str(data_list['weather'][0]['icon']),
        }
        print(data_dict)
    else:
        data_dict = {}

    return render(request, 'main/index.html', data_dict)
