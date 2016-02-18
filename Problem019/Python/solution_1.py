#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Counting Sundays
Problem 19

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to  31 Dec 2000)?
"""


# 0 - SUNDAY
# 1 - MONDAY
# 2 - THIRDDAY
# 3 - WEDNESDAY
# 4 - THURSDAY
# 5 - FRIDAY
# 6 - SATURDAY

days_dic = {
    0: 'SUNDAY',
    1: 'MONDAY',
    2: 'THIRDDAY',
    3: 'WEDNESDAY',
    4: 'THURSDAY',
    5: 'FRIDAY',
    6: 'SATURDAY',
}


def howmanysundays(days, day):
    some_incredible_stuff = int(days - (7 - day) > 28 or day == 0 and days > 28)
    sundays_in_the_month = days // 7 + some_incredible_stuff
    return sundays_in_the_month


def is_leap(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def solution(first_day):
    months_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    interval = range(1900, 2000 + 1)
    day = 1  # MONDAY (first day of year 1900)
    firsts = 0
    for year in interval:
        leap = is_leap(year)
        for month, days in sorted(months_days.items()):
            if month == 2 and leap:
                days += 1
            if year > 1900 and day == first_day:
                firsts += 1
            day += days % 7
            if day > 6:
                day -= 7
    return firsts

print(solution(0))
