"""Wrapper/helper functions for interacting with the MBTAClient library"""
from typing import Any, Dict
from mbtaclient.client.mbta_client import MBTAClient

async def fetch_routes(params: Dict[str, Any]=None):
    """Wrapper for async MBTAClient.fetch_routes()"""
    routes = await MBTAClient().fetch_routes(params)
    return routes

async def fetch_alerts(params: Dict[str, Any]=None):
    """Wrapper for async MBTAClient.fetch_alerts()"""
    alerts = await MBTAClient().fetch_alerts(params)
    return alerts
