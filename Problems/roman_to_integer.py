def romanToInt(roman):
    #how to split roman into the various
    #look for the second charcter of the six subtraction exceptions.
    #if the character that comes before it is
    new_string = []
    dict = {
            "I" : 1,
            "II" : 2,
            "III" : 3,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
            #subtraction exceptions
            "IV" : 4,
            "IX" : 9,
            "XL" : 40,
            "XC" : 90,
            "CD" : 400,
            "CM" : 900
                      }
    answer = 0
    for ind, char in enumerate(roman):
        prev_char = roman[ind - 1]
        if char == "V":
            if prev_char == "I":
                new_string[ind - 1] = 4
                answer = sum(new_string)
            else:
                new_string.append(dict[char])
                answer = sum(new_string)

        else:
            new_string.append(dict[char])
            answer = sum(new_string)

    return answer
