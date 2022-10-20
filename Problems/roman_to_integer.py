def romanToInt(roman):
    dict = {
            "I" : 1,
            "II" : 2,
            "III" : 3,
            "IV" : 4,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
           }
    sum = 0
    for char in roman:
        sum = sum + dict[char]

    return sum
