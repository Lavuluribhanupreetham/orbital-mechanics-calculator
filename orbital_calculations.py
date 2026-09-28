"""
Orbital Calculations Module
============================
Functional Module 1.
Physics calculations for a circular Earth orbit:
    - Circular orbital velocity
    - Escape velocity
    - Orbital period
Input:  altitude above Earth's surface, in kilometres (float, >= 0)
Output: velocity in km/s, or period in minutes (float)
"""
import math
EARTH_RADIUS_KM = 6371        
EARTH_MU = 398600.4418        
def _orbit_radius(altitude: float) -> float:
    if altitude < 0:
        raise ValueError("Altitude cannot be negative.")
    return EARTH_RADIUS_KM + altitude
def orbital_velocity(altitude: float) -> float:
    radius = _orbit_radius(altitude)
    return math.sqrt(EARTH_MU / radius)
def escape_velocity(altitude: float) -> float:
    radius = _orbit_radius(altitude)
    return math.sqrt((2 * EARTH_MU) / radius)
def orbital_period(altitude: float) -> float:
    radius = _orbit_radius(altitude)
    period_seconds = 2 * math.pi * math.sqrt(radius ** 3 / EARTH_MU)
    return period_seconds / 60