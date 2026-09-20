"""Problem 3 - Social Network."""

import csv


def add_user(sn: dict, username: str, fullname: str) -> bool:
    """Add a new user to the social network.

    Return True if the user was added successfully.
    Return False if the username already exists.
    """
    try:
        if username in sn:
            return False

        sn[username] = (fullname, [])
        return True

    except (TypeError, AttributeError) as error:
        print(f"Error adding user: {error}")
        raise


def add_friend(sn: dict, user1: str, user2: str) -> bool:
  
    try:
        if user1 not in sn or user2 not in sn:
            return False

        # Prevent a user from becoming their own friend.
        if user1 == user2:
            return False

        # Add user2 to user1's friend list.
        if user2 not in sn[user1][1]:
            sn[user1][1].append(user2)

        # Add user1 to user2's friend list.
        if user1 not in sn[user2][1]:
            sn[user2][1].append(user1)

        return True

    except (TypeError, KeyError, IndexError) as error:
        print(f"Error adding friendship: {error}")
        raise


def get_friends(sn: dict, user1: str, distance: int) -> list:
   
    try:
        if user1 not in sn or distance <= 0:
            return []

        visited = {user1}
        current_level = [user1]
        result = []

        for _ in range(distance):
            next_level = []

            for user in current_level:
                for friend in sn[user][1]:

                    if friend not in visited:
                        visited.add(friend)
                        result.append(friend)
                        next_level.append(friend)

            current_level = next_level

            # Stop early if there are no more users to visit.
            if not current_level:
                break

        return result

    except (TypeError, KeyError, IndexError) as error:
        print(f"Error getting friends: {error}")
        raise


def save_network(filename: str, sn: dict) -> None:
    """Save the social network dictionary to a CSV file."""
    try:
        with open(
            filename,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.writer(file)

            for username, data in sn.items():
                fullname = data[0]
                friends = data[1]

                writer.writerow(
                    [username, fullname] + friends
                )

    except OSError as error:
        print(f"Error saving network: {error}")
        raise


def load_network(filename: str) -> dict:
    """Load and return a social network from a CSV file."""
    try:
        sn = {}

        with open(
            filename,
            "r",
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.reader(file)

            for row in reader:

                if len(row) >= 2:
                    username = row[0]
                    fullname = row[1]
                    friends = row[2:]

                    sn[username] = (
                        fullname,
                        friends
                    )

        return sn

    except OSError as error:
        print(f"Error loading network: {error}")
        raise


def main() -> None:
    """Test all Problem 3 social network functions."""

    # Original social network from the problem.
    sn = {
        "alice": (
            "Alice Smith",
            ["maria"]
        ),

        "maria": (
            "Maria Cortez",
            ["alice", "joe", "david"]
        ),

        "joe": (
            "Joseph Adams",
            ["maria", "eve"]
        ),

        "eve": (
            "Evelyn Cooper",
            ["joe"]
        ),

        "david": (
            "David Benson",
            ["maria"]
        )
    }

    print("ORIGINAL NETWORK")
    print("----------------")
    print(sn)

    # Test get_friends().
    print("\nALICE - DISTANCE 1")
    print("------------------")
    print(get_friends(sn, "alice", 1))

    print("\nALICE - DISTANCE 2")
    print("------------------")
    print(get_friends(sn, "alice", 2))

    print("\nALICE - DISTANCE 3")
    print("------------------")
    print(get_friends(sn, "alice", 3))

    # Test invalid username.
    print("\nINVALID USER")
    print("------------")
    print(get_friends(sn, "unknown", 2))

    # Test add_user().
    print("\nADD BOB")
    print("-------")

    result = add_user(
        sn,
        "bob",
        "Bob Johnson"
    )

    print(result)

    # Try adding Bob again.
    print("\nADD BOB AGAIN")
    print("-------------")

    result = add_user(
        sn,
        "bob",
        "Bob Johnson"
    )

    print(result)

    # Test add_friend().
    print("\nADD BOB AND ALICE AS FRIENDS")
    print("----------------------------")

    result = add_friend(
        sn,
        "bob",
        "alice"
    )

    print(result)

    print("\nBob's friends:")
    print(sn["bob"][1])

    print("Alice's friends:")
    print(sn["alice"][1])

    # Test invalid friendship.
    print("\nINVALID FRIENDSHIP")
    print("------------------")

    result = add_friend(
        sn,
        "bob",
        "unknown"
    )

    print(result)

    # Test save_network().
    print("\nSAVE NETWORK")
    print("------------")

    save_network(
        "social_network.csv",
        sn
    )

    print("Network saved to social_network.csv")

    # Test load_network().
    print("\nLOAD NETWORK")
    print("------------")

    loaded_network = load_network(
        "social_network.csv"
    )

    print(loaded_network)


if __name__ == "__main__":
    main()