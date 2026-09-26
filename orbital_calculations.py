"""
Orbital Calculations Module
============================
Functional Module 1.
Core physics calculations for a circular Earth orbit:
    - Circular orbital velocity
    - Escape velocity
    - Orbital period
Input:  altitude above Earth's surface, in kilometres (float, >= 0)
Output: velocity in km/s, or period in minutes (float)
"""
import math
EARTH_RADIUS_KM = 6371        # Mean Earth radius (km)
EARTH_MU = 398600.4418        # Earth's standard gravitational parameter (km^3/s^2)
def _orbit_radius(altitude: float) -> float:
    """Convert an altitude above the surface into a radius from Earth's centre.
    Raises ValueError if the altitude is negative (input validation /
    error-handling strategy, per the non-functional requirements).
    """
    if altitude < 0:
        raise ValueError("Altitude cannot be negative.")
    return EARTH_RADIUS_KM + altitude
def orbital_velocity(altitude: float) -> float:
    """Circular orbital velocity (km/s) at a given altitude."""
    radius = _orbit_radius(altitude)
    return math.sqrt(EARTH_MU / radius)
def escape_velocity(altitude: float) -> float:
    """Escape velocity (km/s) at a given altitude."""
    radius = _orbit_radius(altitude)
    return math.sqrt((2 * EARTH_MU) / radius)
def orbital_period(altitude: float) -> float:
    """Orbital period (minutes) at a given altitude."""
    radius = _orbit_radius(altitude)
    period_seconds = 2 * math.pi * math.sqrt(radius ** 3 / EARTH_MU)
    return period_seconds / 60