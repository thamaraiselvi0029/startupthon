from dataclasses import dataclass
from math import radians, sin, cos, sqrt, atan2


@dataclass(frozen=True)
class Hospital:
    name: str
    latitude: float
    longitude: float


HOSPITALS = [
    Hospital("City Hospital", 13.0827, 80.2707),
    Hospital("Government Hospital", 13.0674, 80.2376),
    Hospital("Apollo Hospital", 13.0067, 80.2570),
    Hospital("Fortis Hospital", 13.0319, 80.2433),
]


def calculate_distance(
    latitude1: float,
    longitude1: float,
    latitude2: float,
    longitude2: float
) -> float:
    """Calculate distance between two coordinates in km."""

    earth_radius_km = 6371.0

    lat1 = radians(latitude1)
    lat2 = radians(latitude2)
    delta_lat = radians(latitude2 - latitude1)
    delta_lon = radians(longitude2 - longitude1)

    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1) * cos(lat2) * sin(delta_lon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius_km * c


def find_nearby_hospitals(
    latitude: float,
    longitude: float,
    max_distance_km: float = 20.0
):
    """Find hospitals within the given distance."""

    nearby = []

    for hospital in HOSPITALS:
        distance = calculate_distance(
            latitude,
            longitude,
            hospital.latitude,
            hospital.longitude
        )

        if distance <= max_distance_km:
            nearby.append({
                "name": hospital.name,
                "latitude": hospital.latitude,
                "longitude": hospital.longitude,
                "distance_km": round(distance, 2)
            })

    nearby.sort(key=lambda hospital: hospital["distance_km"])

    return nearby
