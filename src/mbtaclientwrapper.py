"""Wrapper/helper functions for interacting with the MBTAClient library"""
from typing import Any, Dict
from mbtaclient.client.mbta_client import MBTAClient

async def fetch_routes(params: Dict[str, Any]=None):
    """Wrapper for MBTAClient.fetch_routes()"""
    routes = await MBTAClient().fetch_routes(params)
    return routes[0]

async def fetch_alerts(params: Dict[str, Any]=None):
    """Wrapper for MBTAClient.fetch_alerts()"""
    alerts = await MBTAClient().fetch_alerts(params)
    return alerts[0]

async def fetch_schedules(params: Dict[str, Any]=None):
    """Wrapper for MBTAClient.fetch_schedules()"""
    schedules = await MBTAClient().fetch_schedules(params)
    return schedules[0]

async def fetch_stops(params: Dict[str, Any]=None):
    """Wrapper for MBTAClient.fetch_stops()"""
    stops = await MBTAClient().fetch_stops(params)
    return stops[0]