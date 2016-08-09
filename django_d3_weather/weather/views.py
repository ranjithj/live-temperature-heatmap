from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .data import US_states_lat_long
from django.conf import settings
import requests


# Create your views here.


def home(request):

    if request.method == 'GET':
        context = {'data':2}
        return render(request, "index.html", context)

def weatherAPI(request):

    if request.is_ajax():
        #import pdb; pdb.set_trace();
        print("request is a ajax call")

        context = []
        API_KEY = settings.API_KEY
        for key in US_states_lat_long:
            API_URL = 'http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&APPID={2}'.format(US_states_lat_long[key]["lat"], US_states_lat_long[key]["lon"], API_KEY)
            print(API_URL)
            resp = requests.get(url=API_URL)
            datum = {}
            datum["abbr"] = key
            datum["temp"] = resp.json()["main"]["temp"]
            datum["state"] = US_states_lat_long[key]["state"]
            context.append(datum)

        print(context)
        return JsonResponse(context, safe=False)

