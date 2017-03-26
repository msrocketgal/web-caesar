def encrypt(text, rot):
    """ Write one more function called encrypt(text, rot), which receives as input
    a string and an integer & will return the result of rotating each letter in
    the text by rot places to the right. """
    resultText = ""
    for ltr in text:
        resultText += (rotate_character(ltr,rot))
    return resultText


def alphabet_position(letter):
    """ write a function alphabet_position(letter), which receives a letter (that is,
    a string with only one alphabetic character) and returns the 0-based numerical
    position of that letter within the alphabet. """

    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    return int(alphabet.find(letter))


def rotate_character(char, rot):
    """ write helper function rotate_character(char, rot) which receives
    a character char (that is, a string of length 1), and an integer rot.
    Your function should return a new string of length 1, the result of rotating
    char by rot number of places to the right."""
    import string
    alphabet = ("abcdefghijklmnopqrstuvwxyz")
    if char.lower() not in string.ascii_lowercase:
        return char
    if char == char.upper():
        uCase = True
    else:
        uCase = False
    lChar = char.lower()
    newCharPos = alphabet_position(lChar) + int(rot)
    while newCharPos > 25:
        newCharPos = newCharPos - 26
    newChar = alphabet[newCharPos]
    if uCase:
        newChar = newChar.upper()
    return newChar
