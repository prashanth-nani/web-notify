import requests
import time
import sys
import os
from subprocess import call
from requests.exceptions import SSLError

audioFilePath = os.path.join(os.getcwd(), "sound.mp3")
websiteUrl = str(input("Enter the website url: "))
decision = "x"

try:
    r = requests.get(websiteUrl.strip())
except SSLError:
    print("The website's Security certificate could not be verified.\n It is harmful. Do you still want to continue? (Y/N)")
    decision = input()
    if decision.lower() is "y" or "yes":
        r = requests.get(websiteUrl.strip(), verify=False)
    elif decision.lower() is "n" or "no":
        exit()
    else:
        print("Please enter either 'Y' or 'N' and try again\n")
        exit()

originalSiteContent = r.content

while True:
    try:
        r = requests.get(websiteUrl.strip())
    except SSLError:
        r = requests.get(websiteUrl.strip(), verify=False)

    newSiteContent = r.content

    if newSiteContent != originalSiteContent:
        if sys.platform == "win32":
            call("start "+audioFilePath, shell=True)
        exit()
    time.sleep(3)