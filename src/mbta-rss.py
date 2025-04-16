import asyncio
import dominate
from dominate.tags import *
from flask import Flask
from mbtaclient.client.mbta_client import MBTAClient

app = Flask(__name__)

def init_doc(title):
    doc = dominate.document(title=title)

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(id='header'):
            p('TITLE')

    return doc

async def fetch_alerts():
    alerts = await MBTAClient().fetch_alerts()
    return alerts

@app.route("/")
def hello_world():
    doc = init_doc("Home")
    return doc

@app.route("/alerts")
def alerts():
    doc = init_doc('Alerts')
    alerts = asyncio.run(fetch_alerts())
    for alert in alerts[0]:
        doc.add(h2(alert.short_header))
        if alert.description != None:
            doc.add(p(alert.description))
    return str(doc)