def pangrams(s):
    letters_seen = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for letter in s.lower():
        letters_seen[letter] = True

    for letter in alphabet:
        if letter not in letters_seen:
            return "not pangram"

    return "pangram"


if __name__ == "__main__":
    s = input()

    print(pangrams(s))
