# ======================================================
# NUMBER → ROMAN
# ======================================================

def int_to_roman(num):

    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]

    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]

    roman = ""
    i = 0

    while num > 0:
        count = num // values[i]
        roman += symbols[i] * count
        num -= values[i] * count
        i += 1

    return roman


# ======================================================
# ROMAN → NUMBER
# ======================================================

def roman_to_int(s):

    roman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    total = 0
    prev = 0

    try:
        for char in reversed(s.upper()):
            value = roman[char]

            if value < prev:
                total -= value
            else:
                total += value

            prev = value

        return total

    except KeyError:
        return None