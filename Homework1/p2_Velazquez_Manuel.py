def find_Pythagorean(n):
    """Return all Pythagorean triples with values from 1 through n."""

    triples = []

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):

                if a ** 2 + b ** 2 == c ** 2:
                    triples.append((a, b, c))

    return triples


n = int(input("Enter a positive integer: "))

result = find_Pythagorean(n)

for triple in result:
    print(triple)
    