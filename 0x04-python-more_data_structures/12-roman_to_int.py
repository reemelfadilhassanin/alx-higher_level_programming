#!/usr/bin/python3

def roman_to_int(roman_string) :
    if not roman_string or not isinstance(roman_string, str):
        return 0
   

    roman_dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000}

    result = 0
    i = 0
    while i < len(roman_string):
        current_value = roman_dec.get(roman_string[i], 0)

        if i + 1 < len(roman_string):
            next_value = roman_dec.get(roman_string[i + 1], 0)
            if current_value >= next_value:
                result += current_value
                i += 1
            else:
                result += next_value - current_value
                i += 2
        else:
            result += current_value
            i += 1

    return result
