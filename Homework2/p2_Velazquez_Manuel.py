"""Problem 2 - Comprehensions."""


def main() -> None:
    """Test list and dictionary comprehensions."""

    # Part A
    result_a = [
        (a, b, c, d)
        for a in range(1, 11)
        for b in range(1, 11)
        for c in range(1, 11)
        for d in range(1, 11)
        if len({a, b, c, d}) == 4
        and a**2 + b**2 == c**2 + d**2
    ]

    print("Part A:")
    print(result_a)

    # Part B
    words = ["One", "SEVEN", "three", "two", "Ten"]

    result_b = [
        (word.lower(), len(word))
        for word in words
        if len(word) < 5
    ]

    print("\nPart B:")
    print(result_b)

    # Part C
    names = [
        "Christopher Ashton Kutcher",
        "Elizabeth Stamatina Fey"
    ]

    result_c = [
        f"{parts[0]} {parts[1][0]}. {parts[2]}"
        for name in names
        for parts in [name.split()]
    ]

    print("\nPart C:")
    print(result_c)

    # Part D
    lst1 = ["Spam", "Trams", "Elbows", "Tops", "Astral"]
    lst2 = [
        "Bowels",
        "Sample",
        "Altars",
        "Stop",
        "Course",
        "Smart"
    ]

    result_d = [
        (w1, w2)
        for w1 in lst1
        for w2 in lst2
        if sorted(w1.lower()) == sorted(w2.lower())
    ]

    print("\nPart D:")
    print(result_d)

    # Part E
    s = ["one", "two", "three"]

    result_e = {
        word: len(word)
        for word in s
    }

    print("\nPart E:")
    print(result_e)

    # Part F
    text = "Hello world"

    result_f = {
        index: character
        for index, character in enumerate(text)
        if character.lower() in "aeiou"
    }

    print("\nPart F:")
    print(result_f)


if __name__ == "__main__":
    main()