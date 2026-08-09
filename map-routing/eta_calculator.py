def calculate_eta(distance_km: float, speed_kmph: float) -> float:
    """
    Calculate estimated travel time in minutes.

    distance_km: distance in kilometers
    speed_kmph: average speed in km/h
    """
    if distance_km < 0:
        raise ValueError("Distance cannot be negative")

    if speed_kmph <= 0:
        raise ValueError("Speed must be greater than zero")

    eta_hours = distance_km / speed_kmph
    eta_minutes = eta_hours * 60

    return round(eta_minutes, 2)


def calculate_eta_with_traffic(
    distance_km: float,
    speed_kmph: float,
    traffic_factor: float = 1.0
) -> float:
    """Calculate ETA after applying a traffic factor."""

    base_eta = calculate_eta(distance_km, speed_kmph)

    if traffic_factor < 1:
        raise ValueError("Traffic factor must be at least 1")

    return round(base_eta * traffic_factor, 2)
