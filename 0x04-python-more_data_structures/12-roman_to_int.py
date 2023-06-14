#!/usr/bin/python3

def roman_to_int(roman_string):
    """converts a roman numeral to an integer from 1 to 3999
    Args:
        roman_string (str): string of roman numeral
    Return:
        integer (int): integer of the roman numeral
    Desc:
        roman literals include
        I -> 1
        V -> 5
        X -> 10
        L -> 50
        C -> 100
        D -> 500
        M -> 1000
        To solve this we will create some possible numerals
        and their value and some special values like 4, 9, 40,
        90, 400, 900. Then scan through the given string and with
        a substring present we take its value and check for the next,
        and next, and adds its value to the result
    """
    roman = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    num = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and roman_string[i:i + 2] in roman:
            num += roman[roman_string[i:i + 2]]
            i += 2
        else:
            num += roman[roman_string[i]]
            i += 1
    return num

