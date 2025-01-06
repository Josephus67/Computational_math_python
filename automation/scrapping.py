import requests
from bs4 import BeautifulSoup  as bs

url = 'https://josephus67.github.io/AMASSAH-LODGE/home/index.html'

response = requests.get(url,headers={'Accept':'text/html'})

passed_response = bs(response.text,'html.parser')

print(passed_response.prettify())

