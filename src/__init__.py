import asyncio
import logging
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from mbtaclient.client.mbta_client import MBTAClient
from mbtaclient.models.mbta_alert import MBTAAlert
from mbtaclient.models.mbta_route import MBTARoute
from mbtaclient.models.mbta_schedule import MBTASchedule
from mbtaclient.models.mbta_stop import MBTAStop
from .mbtaclientwrapper import *

logging.basicConfig(filename='mbtarss.log', level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    """Homepage route"""
    return render_template("index.html")

@app.route("/alerts", defaults={'route': None})
@app.route("/alerts/<route>")
def alerts(route):
    """Alerts index route. If route is not None only alerts on the specified route(s) will be displayed"""
    a = asyncio.run(fetch_alerts({} if route is None else {'route': route}))
    return render_template("alerts.html", alerts=a)

@app.route("/alert/<alert_id>")
def alert(alert_id):
    """Alert single display route. Displays the contents of the alert with the given id"""
    a = asyncio.run(fetch_alerts({'id': alert_id}))[0]
    stops = asyncio.run(fetch_stops({'id': [e.stop_id for e in a.informed_entities]}))[0]
    return render_template("alert.html", alert=a, stops=stops)

@app.route("/schedule/<route>")
def schedule(route):
    """Alert single display route. Displays the contents of the alert with the given id"""
    a = asyncio.run(fetch_schedules({'route': route}))
    return render_template("schedule.html", schedule=a, route=route)