from twython import Twython, TwythonError
import random
import sys
import os
import time
import urllib
import string
import random
import filecmp
import shutil
import check



#Pillow

#authorization in Twitter and clarifai
from clarifai import rest
from clarifai.rest import ClarifaiApp

from keys import *

app = ClarifaiApp(CLIENT_ID, CLIENT_SECRET)
model = app.models.get("general-v1.3")



def id_generator(size=5, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)



