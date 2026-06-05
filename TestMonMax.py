#!/usr/bin/env python3

def leap_year(year):
    if year % 400 ==0:
        return True
    if year % 100 ==0:
        return False
    if year % 4 ==0:
        return True
    return False

def mon_max(month, year):
    # Determine February length based on leap year
    if leap_year(year):
        feb_days = 29
    else:
        feb_days = 28

    # Dictionary of months
    month_lengths = {
        1: 31,
        2: feb_days,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    return month_lengths[month]
