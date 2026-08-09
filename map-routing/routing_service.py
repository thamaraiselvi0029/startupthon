from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2
from abc import ABC, abstractmethod


@dataclass(frozen=True)
class Coordinate:
    latitude: float
    longitude: float


@dataclass
class RouteResult:
    distance_km: float


def calculate_distance(start: Coordinate, end: Coordinate) -> float:
    """Calculate straight-line distance between two coordinates in km."""
    earth_radius_km = 6371.0

    lat1 = radians(start.latitude)
    lat2 = radians(end.latitude)
    delta_lat = radians(end.latitude - start.latitude)
    delta_lon = radians(end.longitude - start.longitude)

    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_km * c


class RouteService(ABC):
    """Abstraction for future map/routing APIs."""

    @abstractmethod
    def get_route(
        self,
        start: Coordinate,
        end: Coordinate
    ) -> RouteResult:
        pass


class MockRouteService(RouteService):
    """Routing service using coordinate-based mock calculations."""

    def get_route(
        self,
        start: Coordinate,
        end: Coordinate
    ) -> RouteResult:
        distance = calculate_distance(start, end)
        return RouteResult(distance_km=round(distance, 2))
