import requests
from bs4 import BeautifulSoup

def test():
    return "Test"

class dl:
    def opensea(link):
        list = link.split("/")[4:]
        address = list[0]
        id = list[1]
        return "Address: {0}, ID: {1}".format(address,id)