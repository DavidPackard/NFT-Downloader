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
        imageurl = data['image_original_url']
        animurl = data['animation_url']
        #print(data)
        return imageurl, animurl, data

class dl:
    def image(link,dir):
        try:
            list = link.split("/")
            filename = dir + "\\" + str(list[-1:]).replace('[', '').replace(']', '').replace("'", '')
            r = requests.get(link, stream=True)
            if '.' not in filename[-4:]:
                f = open('{0}.png'.format(filename), 'wb')
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
                return '{0}.png'.format(filename)
        except:
            return 'Not an Image, Skipping Download Attempt'
    
    def animation(link,dir):
        try:
            print(link)
            list = link.split("/")
            print(list)
            filename = dir + "\\" + link.replace('[', '').replace(']', '').replace("'", '')
            r = requests.get(link, stream=True)
            if '.' not in filename[-4:]:
                f = open('{0}.png'.format(filename), 'wb')
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
                return 'No Dot, {0}.png'.format(filename)
            else: 
                name = list[-1]
                print(name)
                print('{1}\{0}'.format(name, dir))
                f = open('{0}\{1}'.format(dir, name), 'wb')
                for chunk in r.iter_content(chunk_size=8192): 
                    f.write(chunk)
                return '{1}\{0}'.format(name, dir)
        except:
            return 'Not an Animation, Skipping Download Attempt'