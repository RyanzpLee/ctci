def isUnique(string):
    # Using Hash Table
    # Hash table lookup is O(1), and we will have at most 26 characters
    # Iterate through string, at worst the whole length, so O(n), n = len(s)
    dict = {}

    if not string:
        return True

    for s in string:
        if s in dict:
            return False
        else:
            dict[s] = 1
    return True


def isUniqueBit(string):
    # Using bitwise operators
    check = 0

    for s in string:
        # convert into ascii value by substracting a
        val = ord(s) - ord("a")

        # When you 'And' a 1 and 1, you will return 1 (True), which is greater than 0
        # which signifies a duplicate character
        if (check & (1 << val)) > 0:
            return False

        # Add on a letter to the check
        check |= 1 << val
    return True


string = "bbcdefga"

print(isUniqueBit(string))