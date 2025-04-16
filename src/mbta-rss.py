import asyncio
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from mbtaclient.client.mbta_client import MBTAClient

app = Flask(__name__)
Bootstrap(app)

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
def index():
    return render_template("index.html")

@app.route("/alerts")
def alerts():
    alerts = asyncio.run(fetch_alerts())[0]
    return render_template("alerts.html", alerts=alerts)