### Path to pull libraries from
import sys

rundir = sys.path[0]
new_path = '{0}\lib'.format(rundir)
if new_path not in sys.path:
    sys.path.append(new_path)

### Import Libraries
import modules
from decouple import config
print(modules.test())

### Set Secrets from ENV
# None required yet









### Downloader Script
#Import URLs from file
with open("{0}/url.txt".format(rundir), "r") as file:
    links = file.readlines()
    links = [line.rstrip() for line in links]

#Parse URLs
for link in links:
    list = link.split("/")[4:]
    address = list[0]
    id = list[1]
    # https://opensea.io
    if link[:18] == "https://opensea.io":
        #print(modules.info.opensea(link))
        print(modules.dl.image(modules.info.opensea(link)))