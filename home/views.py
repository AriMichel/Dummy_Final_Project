import requests
from django.shortcuts import render, redirect
from .models import UserLocation
from decouple import config

def landing_page(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        UserLocation.objects.create(location=location)
        return redirect('response_page')
    
    return render(request, 'landing_page.html')
def response_page(request):
    user_location = UserLocation.objects.latest('id')
    location = user_location.location
    
    # Make API call to retrieve weather information
    weather_data = get_weather_data(location)
    
    # Extract required weather data
    temperature = weather_data['current']['temp_c']
    description = weather_data['current']['condition']['text']
    time_data = weather_data['location']['localtime']
         
    context = {
        'location': location,
        'temperature': temperature,
        'description': description,
        'local_time': time_data,
    }
    
    return render(request, 'response_page.html', context)
    

def get_weather_data(location):
    # Make an API call to retrieve weather information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = config('WEATHER_API_KEY')
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data









'''def get_local_time_data(location):
    # Make an API call to retrieve local time information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = 'API_KEY'
    url = f'https://worldtimeapi.org/api/timezone/{location}'
    response = requests.get(url)
    time_data = response.json()
    return time_data'''



'''

# Create your views here.
import requests
from django.shortcuts import render, redirect
from .models import UserLocation

def landing_page(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        UserLocation.objects.create(location=location)
        return redirect('response_page')
    
    return render(request, 'landing_page.html')

def response_page(request):
    user_location = UserLocation.objects.latest('id')
    location = user_location.location
    
    # Make API calls to retrieve weather and time information
    weather_data = get_weather_data(location)
    #time_data = get_local_time_data(location)

    # Extract relevant information from API responses
    weather_info = extract_weather_info(weather_data)
    local_time = extract_local_time(time_data)
    
    context = {
        'location': location,
        'weather': weather_info,
        'time': local_time,
    }
    
    return render(request, 'response_page.html', context)

def get_weather_data(location):
    # Make an API call to retrieve weather information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = '42b335084d884b26a4861433232306'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}&aqi=no'
    response = requests.get(url)
    weather_data = response.json()
    return weather_data

def extract_weather_info(weather_data):
    # Extract the relevant weather information from the API response
    # and return it as a dictionary or any other suitable format
    weather_info = {
        'temperature': weather_data['current']['temp_c'],
        'description': weather_data['condition'][0]['text'],
        # Add more fields as needed
    }
    time_data= {
        'City': weather_data['location']["name"],
        'localtime': weather_data['location']['localtime']
    }
    #return time_data
    return weather_info
'''
'''def get_local_time_data(location):
    # Make an API call to retrieve local time information based on the location
    # Replace 'API_KEY' with your actual API key
    api_key = 'API_KEY'
    url = f'https://worldtimeapi.org/api/timezone/{location}'
    response = requests.get(url)
    time_data = response.json()
    return time_data

def extract_local_time(time_data):
    # Extract the local time information from the API response
    # and return it in a suitable format
    local_time = time_data['datetime']
    return local_time'''