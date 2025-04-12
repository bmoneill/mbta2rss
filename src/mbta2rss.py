from datetime import datetime
import requests

API_URL = 'https://api-v3.mbta.com/'
API_KEY = ''

""" Sends a request to the API and return the JSON output """
def retrieve_from_api(req):
    return requests.get('https://api-v3.mbta.com/' + req).json()

""" Facilitates conversion of alerts from the JSON API into the desired format. """
def get_alerts(driver, route, time):
    driver.print_start()

    req_str = 'alerts'
    character = '?'

    if time != None:
        # only list alerts in effect at a given time
        req_str += character + 'filter[datetime]=' + time
        character = '&'
    if API_KEY != None:
        # use an API key for more requests per minute
        req_str += character + 'api_key=' + API_KEY
        character = '&'
    if route != None:
        # filter to certain routes
        req_str += character + 'filter[route]=' + route
        character = '&'

    # retrieve API result using the formatted request
    alerts = retrieve_from_api(req_str)

    for alert in alerts['data']:
        attributes = alert['attributes']
        desc = ''
        effect = ''
        categories = [] # TODO currently unused, how to implement?
        guid = alert['id']

        header = attributes['short_header'] # this should always be non-empty
        long_header = attributes['header'] # this should always be non-empty
        dt = datetime.fromisoformat(attributes['created_at'])
        date = dt.strftime('%m-%d-%Y %I:%M %p')

        if attributes['description'] != None:
            desc = attributes['description']

        if attributes['effect'] != None:
            effect = 'Effect: ' + attributes['effect']

        # print using given driver
        driver.print_item(header, long_header, desc, effect, date, categories, guid)

    driver.print_end()

"""
List stops for each route in a list (only works for Markdown, output
is hardcoded in that format currently).
"""
def get_stoplist(routes):
    if routes == None:
        print("route list must be provided when listing stops")
        exit(1)

    driver.print_start()
    for route in routes.split(','):
        reqstr = 'stops?filter[route]=' + route
        if API_KEY != None:
            reqstr += '&api_key=' + API_KEY
        stoplist = retrieve_from_api(reqstr)
        print("## Route: " + route)
        for stop in stoplist['data']:
            print("* " + stop['attributes']['name'])
    driver.print_end()
