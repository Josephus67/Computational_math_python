
import requests
from bs4 import BeautifulSoup as bs

github_user = input("Please Enter the github username :")

github_url = 'https://github.com/' + github_user

r = requests.get(github_url)

soup = bs(r.content,'html.parser')

profile_image = soup.find('img',{'class':"avatar avatar-user width-full border color-bg-default"})["src"]

print(profile_image)



import requests
from bs4 import BeautifulSoup as bs

def get_github(userId):
    github_url = 'https://github.com/'+ userId
    make_request = requests.get(github_url)
    soup = bs(make_request.content,'html.parser')
    profile_image = soup.find('img',{'class':"avatar avatar-user width-full border color-bg-default"})['src']
    return profile_image
    
get_github("Josephus67")
