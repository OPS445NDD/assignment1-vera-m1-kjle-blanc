#!/usr/bin/env python3

def leap_year(year):
    #Divisible by 400
    if year % 400 ==0:
        return True

    # Divisible by 100, (not a leap year)
    if year % 100 ==0:
        return False

    # Divisible by 4
    if year % 4 ==0:
        return True

    # If it is not a leap year
    return False
