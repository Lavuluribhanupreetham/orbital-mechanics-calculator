"""
Hohmann Transfer Module
========================
Functional Module 2.
Calculates two-burn Hohmann transfer between two circular earth orbits.
Input:  initial_altitude, final_altitude (km, >= 0, and not equal)
Output: a HohmannResult with velocities, delta-v budget and transfer time
"""
import math
from dataclasses import dataclass
from orbital_calculations import EARTH_MU, _orbit_radius
@dataclass
class HohmannResult:
    velocity_initial: float
    velocity_final: float
    velocity_transfer_1: float
    velocity_transfer_2: float
    delta_velocity_1: float
    delta_velocity_2: float
    total_delta_velocity: float
    transfer_time_in_sec: float
def hohmann_transfer(initial_altitude: float, final_altitude: float) -> HohmannResult:
    if initial_altitude == final_altitude:
        raise ValueError("Initial and final altitudes must be different.")
    initial_orbit_radius = _orbit_radius(initial_altitude)
    final_orbit_radius = _orbit_radius(final_altitude)
    velocity_initial = math.sqrt(EARTH_MU / initial_orbit_radius)
    velocity_final = math.sqrt(EARTH_MU / final_orbit_radius)
    transfer_radius = (initial_orbit_radius + final_orbit_radius) / 2
    velocity_transfer_1 = math.sqrt(EARTH_MU * (2 / initial_orbit_radius - 1 / transfer_radius))
    velocity_transfer_2 = math.sqrt(EARTH_MU * (2 / final_orbit_radius - 1 / transfer_radius))
    delta_velocity_1 = abs(velocity_transfer_1 - velocity_initial)
    delta_velocity_2 = abs(velocity_final - velocity_transfer_2)
    total_delta_velocity = delta_velocity_1 + delta_velocity_2
    transfer_time_in_sec = math.pi * math.sqrt(transfer_radius ** 3 / EARTH_MU)
    return HohmannResult(
        velocity_initial=velocity_initial,
        velocity_final=velocity_final,
        velocity_transfer_1=velocity_transfer_1,
        velocity_transfer_2=velocity_transfer_2,
        delta_velocity_1=delta_velocity_1,
        delta_velocity_2=delta_velocity_2,
        total_delta_velocity=total_delta_velocity,
        transfer_time_in_sec=transfer_time_in_sec)