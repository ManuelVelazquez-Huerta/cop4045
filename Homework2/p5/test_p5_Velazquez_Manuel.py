"""Unit tests for Problem 5."""

import os
import unittest
from datetime import datetime

from p5_Velazquez_Manuel import (
    read_observations,
    station_statistics,
    station_outliers,
    write_statistics,
)


class TestWeatherStations(unittest.TestCase):
    """Test Problem 5 weather station functions."""

    def setUp(self):
        """Create a temporary input file before each test."""
        self.filename = "test_weather.txt"

    def tearDown(self):
        """Delete temporary files after each test."""
        if os.path.exists(self.filename):
            os.remove(self.filename)

        if os.path.exists("test_output.txt"):
            os.remove("test_output.txt")

    def test_multiple_stations(self):
        """Test reading multiple stations."""
        with open(self.filename, "w") as file:
            file.write(
                "Miami,01:00:00 PM 09/20/2026,80\n"
                "Orlando,02:00:00 PM 09/20/2026,75\n"
            )

        observations, errors = read_observations(
            self.filename
        )

        self.assertIn("Miami", observations)
        self.assertIn("Orlando", observations)
        self.assertEqual(errors, [])

    def test_negative_temperature(self):
        """Test a valid negative temperature."""
        with open(self.filename, "w") as file:
            file.write(
                "Alaska,01:00:00 PM 01/01/2026,-20\n"
            )

        observations, errors = read_observations(
            self.filename
        )

        self.assertEqual(
            observations["Alaska"][0][1],
            -20.0
        )

        self.assertEqual(errors, [])

    def test_invalid_temperature(self):
        """Test temperature outside valid range."""
        with open(self.filename, "w") as file:
            file.write(
                "Miami,01:00:00 PM 09/20/2026,200\n"
            )

        observations, errors = read_observations(
            self.filename
        )

        self.assertNotIn("Miami", observations)
        self.assertEqual(len(errors), 1)

    def test_duplicate_observation(self):
        """Test duplicate station and date."""
        with open(self.filename, "w") as file:
            file.write(
                "Miami,01:00:00 PM 09/20/2026,80\n"
                "Miami,01:00:00 PM 09/20/2026,85\n"
            )

        observations, errors = read_observations(
            self.filename
        )

        self.assertEqual(
            len(observations["Miami"]),
            1
        )

        self.assertEqual(len(errors), 1)

    def test_statistics(self):
        """Test min, max, and mean calculations."""

        observations = {
            "Miami": [
                (
                    datetime(2026, 9, 20, 12, 0),
                    70.0
                ),
                (
                    datetime(2026, 9, 20, 13, 0),
                    80.0
                ),
                (
                    datetime(2026, 9, 20, 14, 0),
                    90.0
                ),
            ]
        }

        statistics = station_statistics(
            observations
        )

        self.assertEqual(
            statistics["Miami"],
            (70.0, 90.0, 80.0)
        )

    def test_outlier(self):
        """Test latest temperature above mean."""

        observations = {
            "Miami": [
                (
                    datetime(2026, 9, 20, 12, 0),
                    70.0
                ),
                (
                    datetime(2026, 9, 20, 13, 0),
                    80.0
                ),
                (
                    datetime(2026, 9, 20, 14, 0),
                    100.0
                ),
            ]
        }

        result = station_outliers(
            observations
        )

        self.assertIn("Miami", result)

    def test_write_statistics_sorted(self):
        """Test that stations are written alphabetically."""

        statistics = {
            "Orlando": (60.0, 90.0, 75.0),
            "Miami": (70.0, 100.0, 85.0),
        }

        write_statistics(
            "test_output.txt",
            statistics
        )

        with open(
            "test_output.txt",
            "r"
        ) as file:

            lines = file.readlines()

        self.assertTrue(
            lines[0].startswith("Miami")
        )

        self.assertTrue(
            lines[1].startswith("Orlando")
        )


if __name__ == "__main__":
    unittest.main()