from typing import Any, Dict
from mbtaclient.client.mbta_client import MBTAClient

async def fetch_routes(params: Dict[str, Any]=None):
    routes = await MBTAClient().fetch_routes(params)
    return routes

async def fetch_alerts(params: Dict[str, Any]=None):
    alerts = await MBTAClient().fetch_alerts(params)
    return alerts
