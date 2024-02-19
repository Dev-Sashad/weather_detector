import urllib.request
import json
from urllib.error import HTTPError
from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == "POST":
        city = request.POST.get('location', '')
        print(city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=ad5afcb589e785b27686ccb6ed9ec57e&units=metric"
        try:
            res = urllib.request.urlopen(url.replace(" ",""))
            json_data = json.loads(res.read())
            data = {
                "country_code" : str(json_data['sys']['country']),
                "temp" : str(json_data['main']['temp']),
                "pressure" : str(json_data['main']['pressure']),
                "humidity" : str(json_data['main']['humidity']),
                "coordinate" :'longitude:' + str(json_data['coord']['lon']) + ' , ' + 'latitude:' + str(json_data['coord']['lat']),
            }
            return render(request, 'index.html',{"city":city, "data":data})
        except HTTPError as e:
            print(f"HTTP Error {e.code}: {e.reason}")
            data = {}
            messages.info(request , f"{e.reason}")
            return redirect('index')
        
    else:
        city = ''
        data = {}
        return render(request, 'index.html',{"city":city, "data":data})
