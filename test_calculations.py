"""
Unit tests for orbital_calculations.py and hohmann_transfer.py.
Run with:  python -m unittest test_calculations.py
"""
import unittest
from orbital_calculations import orbital_velocity, escape_velocity, orbital_period
from hohmann_transfer import hohmann_transfer
class TestOrbitalCalculations(unittest.TestCase):
    def test_orbital_velocity_leo(self):
        v = orbital_velocity(400)
        self.assertAlmostEqual(v, 7.66, places=1)
    def test_escape_velocity_ground(self):
        v = escape_velocity(0)
        self.assertAlmostEqual(v, 11.19, places=1)
    def test_orbital_period_leo(self):
        period = orbital_period(400)
        self.assertTrue(90 <= period <= 95)
    def test_negative_altitude_raises(self):
        with self.assertRaises(ValueError):
            orbital_velocity(-100)
class TestHohmannTransfer(unittest.TestCase):
    def test_leo_to_geo(self):
        result = hohmann_transfer(400, 35786)
        self.assertGreater(result.total_delta_velocity, 0)
        self.assertGreater(result.transfer_time_in_sec, 0)
    def test_equal_altitudes_raises(self):
        with self.assertRaises(ValueError):
            hohmann_transfer(500, 500)
if __name__ == "__main__":
    unittest.main()