import requests
from bs4 import BeautifulSoup as bs


def get_soup(url):
    """ """
    page = requests.get(url)
    soup = bs(page.content, "html.parser")

#    g = soup.find_all("ul", {"class" : "arkProductSpecifications"})
    g = soup.find_all("ul", {"class" : "specs-list"})
    print(len(g))
    for item in g:
        print("--------------")
        print(item.prettify())
    
    
