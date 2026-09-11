def find_dup_str(s, n):
    """Return the first duplicated non-overlapping substring of length n."""

    for i in range(len(s) - n + 1):
        substring = s[i:i + n]

        # Start at i + n so the two occurrences cannot overlap.
        for j in range(i + n, len(s) - n + 1):

            if substring == s[j:j + n]:
                return substring

    return ""


s = input("Enter a string: ")
n = int(input("Enter substring length: "))

print(find_dup_str(s, n))
def find_dup_str(s, n):
    """Return the first duplicated non-overlapping substring of length n."""

    for i in range(len(s) - n + 1):
        substring = s[i:i + n]

        for j in range(i + n, len(s) - n + 1):

            if substring == s[j:j + n]:
                return substring

    return ""


def find_max_dup(s):
    """Return the longest duplicated non-overlapping substring."""

    # Two non-overlapping copies cannot each be longer than half the string.
    max_length = len(s) // 2

    for length in range(max_length, 0, -1):

        result = find_dup_str(s, length)

        if result != "":
            return result

    return ""


s = input("Enter a string: ")

print(find_max_dup(s))

find_max_dup("abcdefbcdgh")
find_max_dup("0123456")