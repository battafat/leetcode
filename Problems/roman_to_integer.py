def handle_subtraction(char, prev_char, new_string, ind, dict):
    if char == "V":
        if prev_char == "I":
            print("line 4, ind = ", ind)
            new_string[ind - 1] = 0
            new_string.append(4)
            return new_string

    elif char == "X":
        if prev_char == "I":
            print("line 10, ind = ", ind)
            new_string[ind - 1] = 0
            new_string.append(9)
            return new_string

    elif char == "L":
        if prev_char == "X":
            print("line 16, ind = ", ind)
            new_string[ind - 1] = 0
            new_string.append(40)
            return new_string

    elif char == "C":
        if prev_char == "X":
            print(new_string)
            print("line 19, ind = ", ind)
            new_string[ind - 1] = 0
            new_string.append(90)
            return new_string

    elif char == "D":
        if prev_char == "C":
            print("line 30, ind = ", ind)
            new_string[ind - 1] = 0
            new_string.append(400)
            return new_string

    elif char == "M":
        if prev_char == "C":
            new_string[ind - 1] = 0
            new_string.append(900)
            return new_string

    new_string.append(dict[char])
    return new_string

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
        if ind == 0:
            new_string.append(dict[char])
        else:
            prev_char = roman[ind - 1]
            new_string = handle_subtraction(char, prev_char, new_string, ind, dict)


    return sum(new_string)
