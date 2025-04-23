"""Wrapper/helper functions for interacting with the MBTAClient library"""
from typing import Any, Dict
from mbtaclient.client.mbta_client import MBTAClient
from mbtaclient.models.mbta_alert import MBTAAlert
from mbtaclient.models.mbta_route import MBTARoute
from mbtaclient.models.mbta_schedule import MBTASchedule
from mbtaclient.models.mbta_stop import MBTAStop

async def fetch_routes(params: Dict[str, Any]=None) -> list[MBTARoute]:
    """Wrapper for MBTAClient.fetch_routes()"""
    routes = await MBTAClient().fetch_routes(params)
    return routes[0]

async def fetch_alerts(params: Dict[str, Any]=None) -> list[MBTAAlert]:
    """Wrapper for MBTAClient.fetch_alerts()"""
    alerts = await MBTAClient().fetch_alerts(params)
    return alerts[0]

async def fetch_schedules(params: Dict[str, Any]=None) -> list[MBTASchedule]:
    """Wrapper for MBTAClient.fetch_schedules()"""
    schedules = await MBTAClient().fetch_schedules(params)
    return schedules[0]

async def fetch_stops(params: Dict[str, Any]=None) -> list[MBTAStop]:
    """Wrapper for MBTAClient.fetch_stops()"""
    stops = await MBTAClient().fetch_stops(params)
    return stops[0]
