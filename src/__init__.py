import asyncio
import logging
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from .mbtaclientwrapper import *

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alerts", defaults={'route': None})
@app.route("/alerts/<route>")
def alerts(route):
    a = asyncio.run(fetch_alerts({'route': route}))[0]
    return render_template("alerts.html", alerts=a)

@app.route("/alert/<id>")
def alert(id):
    a = asyncio.run(fetch_alerts(id))[0]
    return render_template("alert.html", alert=a)

@app.route("/routes")
@app.route("/routes/<route>")
def routes():
    r = asyncio.run(fetch_routes())[0]
    return render_template("routes.html", routes=r)