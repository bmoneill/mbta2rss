# File: test.py
# Description: This pulls down all the MBTA alerts and prints them out.
# Author: Ben O'Neill <ben@benoneill.xyz>
# License: GNU GPLv3

import json
import requests

def get_alert_headers():
    alerts = requests.get('https://api-v3.mbta.com/alerts').json()
    i = 1
    for alert in alerts['data']:
        print(str(i) + ": " + alert['attributes']['header'])
        i += 1


get_alert_headers()
