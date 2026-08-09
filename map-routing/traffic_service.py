def apply_traffic_factor(base_eta_minutes: float, traffic_factor: float) -> float:
    """
    Adjust ETA based on traffic.

    traffic_factor:
    1.0 = normal traffic
    1.2 = 20% slower
    1.5 = 50% slower
    """
    if base_eta_minutes < 0:
        raise ValueError("ETA cannot be negative")

    if traffic_factor < 1:
        raise ValueError("Traffic factor must be at least 1")

    return round(base_eta_minutes * traffic_factor, 2)


def get_traffic_factor(level: str) -> float:
    """Return a traffic factor for a traffic level."""

    factors = {
        "low": 1.0,
        "medium": 1.2,
        "high": 1.5,
    }

    level = level.lower()

    if level not in factors:
        raise ValueError("Traffic level must be low, medium, or high")

    return factors[level]
