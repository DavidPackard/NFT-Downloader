import requests
from bs4 import BeautifulSoup
import json

def test():
    return "Custom Modules Library Installed"

class info:
    def opensea(link):
        list = link.split("/")[4:]
        address = list[0]
        id = list[1]
        #return "Address: {0}, ID: {1}".format(address,id)
        request = requests.get('https://api.opensea.io/api/v1/asset/{0}/{1}/'.format(address,id))
        data = request.json()
        imageurl = data['image_url']
        return imageurl

class dl:
    def image(link):
        list = link.split("/")
        filename = list[3:]
        r = requests.get(link)
        if '.' not in filename[-4:]:
            f = open 