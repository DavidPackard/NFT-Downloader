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
opensea_key = config('opensea', default='')









### Downloader Script
#Import URLs from file
with open("{0}/url.txt".format(rundir), "r") as file:
    links = file.readlines()
    links = [line.rstrip() for line in links]

#Parse URLs
for link in links:
    # https://opensea.io
    if link[:18] == "https://opensea.io":
        print(modules.dl.opensea(link))