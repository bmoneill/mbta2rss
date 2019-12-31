# File: mbta2rss.py
# Description: This pulls down all the MBTA alerts and prints them out.
# Author: Ben O'Neill <ben@benoneill.xyz>
# License: GNU GPLv3

import args
import json
import requests

def print_rss_channel_start(title='MBTA Unofficial Alert Feed',
        desc='An unofficial, gratis RSS alert feed for MBTA users.',
        lang='en-us'):
    print('<?xml version="1.0" encoding="utf-8"?>')
    print('<?xml-stylesheet type="text/css" href="rss.css" ?>')
    print('<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">')
    print('<channel>')
    print('<title>' + title + '</title>')
    print('<link>https://gitlab.com/swegbun/mbta-rss</link>')
    print('<description>' + desc + '</description>')
    print('<language>' + lang + '</language>')

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

def retrieve_from_api(req=''):
    return requests.get('https://api-v3.mbta.com/' + req).json()
    #with open(req + '.json') as f:
    #    return json.load(f)

def get_alerts(route='*'):
    alerts = retrieve_from_api('alerts')

    for alert in alerts['data']:
        attributes=alert['attributes']
        title=''
        description=''
        effect=''
        routes_affected=''
        categories=[]
        affected_ledger=[]
        route_affected=False # The route we want if route != '*'

        header='<h2>' + attributes['header'] + '</h3>'

        if attributes['description'] != None:
            description = '<h3>' + attributes['description'] + '</h3>'

        if attributes['effect'] != None:
            effect = '<h3>Effect: ' + attributes['effect'] + '</h3>'

        for affected in attributes['informed_entity']:
            if 'route' in affected:
                if affected['route'] not in affected_ledger:
                    if affected['route'] == route:
                        route_affected = True
                    routes_affected += '<li>' + affected['route'] + '</li>'
                    categories.append(affected['route'])
                    affected_ledger.append(affected['route'])

        if routes_affected == '':
            routes_affected = '<p>Routes affected: None or N/A</p>'
        else:
            routes_affected = '<h3>Routes affected:</h3><ul>' + routes_affected
            routes_affected += '</ul>'

        title=attributes['header']
        if len(title) > 100:
            title = title[:100]

        if (route_affected and route != '*') or route == '*':
            print_rss_item(title, header + description + effect + routes_affected, attributes['created_at'], categories)

if __name__ == '__main__':
    print_rss_channel_start()
    if 'k' in args.flags:
        pass # TODO API key
    if '--route' in args.assignments:
        print("Retrieving for route " + args.assignments['--route'][0])
        route = args.assignments['--route'][0]
        get_alerts(route)
    else:
        get_alerts()
    print_rss_channel_end()
