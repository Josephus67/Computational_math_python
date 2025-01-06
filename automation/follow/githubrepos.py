

def githubRepos(username: str):
    #public repos
    import requests
    from bs4 import BeautifulSoup as bs
    
    url = 'https://github.com/'+username+'?tab=repositories'
    
    response = requests.get(url, headers={'Accept':'text/html'})
    
    passed_response = bs(response.text,'html.parser')
    
    titles = passed_response.find_all('h3',class_="wb-break-all")
    
    for title in titles:
        print(title.text.strip())


githubRepos('Josephus67')