import requests
from pprint import pprint

API_KEY = '8616c09cf64541a3624b996ca4360060'

city : str
city = input('Enter the name of the city: ')

base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'

weather_data = requests.get(base_url).json()
print(weather_data)