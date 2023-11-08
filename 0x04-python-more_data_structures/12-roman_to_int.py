#!/usr/bin/python3
def roman_to_int(roman_string):
        if not isinstance(roman_string, str):
           return 0
        dec = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}
        result = 0
        num = 0
        for i in reversed(roman_string):
         num = dec[i]
         result += num if result < num * 5 else -num
        return result
