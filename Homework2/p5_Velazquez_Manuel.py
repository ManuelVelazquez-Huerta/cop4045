"""Problem 5 - Weather Station Observations."""

import sys
from datetime import datetime


DATE_FORMAT = "%I:%M:%S %p %m/%d/%Y"


def read_observations(filename: str) -> tuple:
    """Read weather observations from a file.

    Return a tuple containing:
    1. A dictionary of valid observations.
    2. A list of error messages.
    """
    observations = {}
    errors = []
    seen = set()

    try:
        with open(filename, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                line = line.strip()

                if not line:
                    continue

                try:
                    parts = line.split(",")

                    # Each line must contain exactly 3 fields.
                    if len(parts) != 3:
                        raise ValueError(
                            "expected station,date,temperature"
                        )

                    station = parts[0].strip()
                    date_string = parts[1].strip()
                    temperature_string = parts[2].strip()

                    # Station cannot be empty.
                    if not station:
                        raise ValueError(
                            "station name is missing"
                        )

                    # Convert the date string to datetime.
                    date = datetime.strptime(
                        date_string,
                        DATE_FORMAT
                    )

                    # Convert temperature to float.
                    temperature = float(
                        temperature_string
                    )

                    # Check valid temperature range.
                    if temperature < -100 or temperature > 150:
                        raise ValueError(
                            "temperature outside valid range"
                        )

                    # Check for duplicate station/date.
                    key = (station, date)

                    if key in seen:
                        raise ValueError(
                            "duplicate station/date"
                        )

                    seen.add(key)

                    # Add station if it does not exist.
                    if station not in observations:
                        observations[station] = []

                    observations[station].append(
                        (date, temperature)
                    )

                except ValueError as error:
                    errors.append(
                        f"Line {line_number}: {error}"
                    )

        # Sort each station's observations by date.
        for station in observations:
            observations[station].sort(
                key=lambda observation: observation[0]
            )

        return observations, errors

    except OSError as error:
        print(f"Error reading file: {error}")
        raise


def station_statistics(observations: dict) -> dict:
    """Return min, max, and mean temperature for each station."""
    statistics = {}

    for station, readings in observations.items():

        temperatures = [
            temperature
            for date, temperature in readings
        ]

        if temperatures:
            minimum = min(temperatures)
            maximum = max(temperatures)
            mean = sum(temperatures) / len(temperatures)

            statistics[station] = (
                minimum,
                maximum,
                mean
            )

    return statistics


def station_outliers(observations: dict) -> dict:
    """Return stations whose latest temperature exceeds the mean."""

    statistics = station_statistics(observations)

    return {
        station: (
            readings[-1][0],
            readings[-1][1],
            statistics[station][2]
        )
        for station, readings in observations.items()
        if readings
        and readings[-1][1] > statistics[station][2]
    }


def write_statistics(
    filename: str,
    statistics: dict
) -> None:
    """Write station statistics to a text file."""

    try:
        with open(filename, "w", encoding="utf-8") as file:

            for station in sorted(statistics):

                minimum, maximum, mean = (
                    statistics[station]
                )

                file.write(
                    f"{station}: "
                    f"min={minimum:.1f}, "
                    f"max={maximum:.1f}, "
                    f"mean={mean:.1f}\n"
                )

    except OSError as error:
        print(f"Error writing file: {error}")
        raise


def main() -> None:
    """Run the weather station program."""

    if len(sys.argv) != 3:
        print(
            "Usage: python p5_Velazquez_Manuel.py "
            "input_file output_file"
        )
        return

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    try:
        observations, errors = read_observations(
            input_filename
        )

        statistics = station_statistics(
            observations
        )

        outliers = station_outliers(
            observations
        )

        write_statistics(
            output_filename,
            statistics
        )

        print("OBSERVATIONS")
        print("------------")
        print(observations)

        print("\nERRORS")
        print("------")

        if errors:
            for error in errors:
                print(error)
        else:
            print("No errors.")

        print("\nSTATISTICS")
        print("----------")

        for station in sorted(statistics):
            minimum, maximum, mean = statistics[station]

            print(
                f"{station}: "
                f"min={minimum:.1f}, "
                f"max={maximum:.1f}, "
                f"mean={mean:.1f}"
            )

        print("\nOUTLIERS")
        print("--------")

        if outliers:
            for station, data in outliers.items():

                date, temperature, mean = data

                print(
                    f"{station}: "
                    f"latest={temperature:.1f}, "
                    f"mean={mean:.1f}, "
                    f"date={date}"
                )
        else:
            print("No outliers.")

        print(
            f"\nStatistics written to "
            f"{output_filename}"
        )

    except OSError:
        print(
            "The program could not access "
            "one of the files."
        )


if __name__ == "__main__":
    main()