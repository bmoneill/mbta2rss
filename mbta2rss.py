# File: mbta2rss.py
# Description: This pulls down all the MBTA alerts and prints them out.
# Author: Ben O'Neill <ben@benoneill.xyz>
# Copyright: Copyright (C) 2019-2020 Ben O'Neill <benoneill.xyz>. Licensed under
# GNU GPL v3.

import argparse
import json
import requests

def print_rss_channel_start(title='MBTA Unofficial Alert Feed',
        desc='An unofficial, gratis RSS alert feed for MBTA users.',
        lang='en-us', link='https://gitlab.com/swegbun/mbta-rss'):
    print('<?xml version="1.0" encoding="utf-8"?>')
    print('<?xml-stylesheet type="text/css" href="rss.css" ?>')
    print('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">')
    print('<channel>')
    print('<title>' + title + '</title>')
    print('<link>' + link + '</link>')
    print('<description>' + desc + '</description>')
    print('<language>' + lang + '</language>') # FIXME does the API even support any other languages?

def print_rss_channel_end():
    print('</channel>')
    print('</rss>')

def print_rss_item(title='Title Placeholder', desc='Description Placeholder',
        date='', categories=''):
    print('<item>')
    print('<title>' + title + '</title>')
    print('<description><![CDATA[' + desc + ']]></description>')
    print('<pubDate>' + date + '</pubDate>')
    for category in categories:
        print('<category>' + category + '</category>')
    print('</item>')

def retrieve_from_api(req):
    return requests.get('https://api-v3.mbta.com/' + req).json()

def get_alerts(key, route):
    req_str = 'alerts'
    if key != None:
        req_str += '?api_key=' + key
    if route != None:
        req_str += '?filter[route]=' + route


    alerts = retrieve_from_api(req_str)
    print(alerts)
    for alert in alerts['data']:
        attributes = alert['attributes']
        title = ''
        description = ''
        effect = ''
        routes_affected = ''
        categories = []
        affected_ledger = []
        route_affected = False # The route we want if route != '*'

        header = '<h2>' + attributes['header'] + '</h3>'

        if attributes['description'] != None:
            description = '<h3>' + attributes['description'] + '</h3>'

        if attributes['effect'] != None:
            effect = '<h3>Effect: ' + attributes['effect'] + '</h3>'

        if routes_affected == '':
            routes_affected = '<p>Routes affected: None or N/A</p>'
        else:
            routes_affected = '<h3>Routes affected:</h3><ul>' + routes_affected
            routes_affected += '</ul>'

        title=attributes['header']
        if len(title) > 100:
            title = title[:100] # prevent really long titles, kind of sloppy but it works I guess

        print_rss_item(title, header + description + effect + routes_affected, attributes['created_at'], categories)

if __name__ == '__main__':
    print_rss_channel_start()
    parser = argparse.ArgumentParser()
    parser.add_argument('-k')
    parser.add_argument('-r')
    args = parser.parse_args()
    key = args.k
    route = args.r
    get_alerts(key, route)
    print_rss_channel_end()
