"""Problem 4 - IMDb Movie Data Analysis."""

import csv


def read_top_rated(filename: str) -> set:
    """Read top-rated movies and return a set of movie keys."""
    movies = set()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = row["Title"].strip()
                year = row["Year"].strip()

                movies.add((title, year))

        return movies

    except OSError as error:
        print(f"Error reading top-rated file: {error}")
        raise


def read_top_grossing(filename: str) -> dict:
    """Read top-grossing movies and return their box-office totals."""
    movies = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                title = row["Title"].strip()
                year = row["Year"].strip()

                money = row["USA Box Office"].strip()

                # Remove dollar signs and commas if present.
                money = money.replace("$", "")
                money = money.replace(",", "")

                movies[(title, year)] = int(money)

        return movies

    except (OSError, ValueError) as error:
        print(f"Error reading top-grossing file: {error}")
        raise


def read_casts(filename: str) -> list:
    """Read movie directors and casts from the cast CSV file."""
    movies = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            # The cast file does NOT contain a header.
            for row in reader:

                if len(row) >= 4:
                    title = row[0].strip()
                    year = row[1].strip()
                    director = row[2].strip()

                    actors = [
                        actor.strip()
                        for actor in row[3:8]
                        if actor.strip()
                    ]

                    movies.append(
                        (
                            title,
                            year,
                            director,
                            actors
                        )
                    )

        return movies

    except OSError as error:
        print(f"Error reading cast file: {error}")
        raise


def display_top_collaborations(
    rated_filename: str,
    casts_filename: str,
    limit: int = 10
) -> None:

    rated_movies = read_top_rated(rated_filename)
    cast_movies = read_casts(casts_filename)

    collaborations = {}

    for title, year, director, actors in cast_movies:

        movie_key = (title, year)

        # Only consider movies in the top-rated list.
        if movie_key in rated_movies:

            for actor in actors:

                pair = (director, actor)

                collaborations[pair] = (
                    collaborations.get(pair, 0) + 1
                )

    ranking = sorted(
        collaborations.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("TOP DIRECTOR / ACTOR COLLABORATIONS")
    print("-----------------------------------")

    for position, (pair, count) in enumerate(
        ranking[:limit],
        start=1
    ):
        director, actor = pair

        print(
            f"{position}. "
            f"{director} / {actor} - "
            f"{count} movies"
        )


def display_top_actors(
    grossing_filename: str,
    casts_filename: str,
    limit: int = 10
) -> None:
    """Display actors ranked by total USA box office."""

    grossing_movies = read_top_grossing(
        grossing_filename
    )

    cast_movies = read_casts(casts_filename)

    actor_totals = {}

    for title, year, director, actors in cast_movies:

        movie_key = (title, year)

        if movie_key in grossing_movies:

            box_office = grossing_movies[movie_key]

            for actor in actors:

                actor_totals[actor] = (
                    actor_totals.get(actor, 0)
                    + box_office
                )

    ranking = sorted(
        actor_totals.items(),
        key=lambda item: item[1],
        reverse=True
    )

    print("\nTOP ACTORS BY TOTAL USA BOX OFFICE")
    print("---------------------------------")

    for position, (actor, total) in enumerate(
        ranking[:limit],
        start=1
    ):

        print(
            f"{position}. "
            f"{actor} - "
            f"${total:,}"
        )


def main() -> None:
    """Test the Problem 4 functions."""

    rated_file = "imdb-top-rated.csv"
    grossing_file = "imdb-top-grossing.csv"
    casts_file = "imdb-top-casts.csv"

    display_top_collaborations(
        rated_file,
        casts_file,
        10
    )

    display_top_actors(
        grossing_file,
        casts_file,
        10
    )


if __name__ == "__main__":
    main()