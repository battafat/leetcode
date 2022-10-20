def romanToInt(roman):
    dict = {"I" : 1, "II" : 2, "III" : 3, "IV" : 4, "V" : 5, "X" : 10}
    sum = 0
    for char in roman:
        sum = sum + dict[char]

    return sum
