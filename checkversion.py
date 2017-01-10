#!/usr/bin/env python

import requests

print requests.__version__

response = requests.get("https://raw.githubusercontent.com/kylecarlstrom/cmput404w17lab1/master/checkversion.py")

print response.status_code

print response.text
