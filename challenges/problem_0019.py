# You are given the following information, but you may prefer to do some research for yourself.
#
# - 1 Jan 1900 was a Monday.
# - Thirty days has September,
# - April, June, and November.
# - All the rest have thirty-one,
# - Saving February alone,
# - Which has twenty-eight, rain or shine.
# - And on leap years, twenty-nine.
# - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
import datetime

this = datetime.datetime.now()
this.day()

class Months:
    Jan = 31
    Feb = 28
    Mar = 31
    Apr = 30
    May = 31
    Jun = 30
    Jul = 31
    Aug = 31
    Sep = 30
    Oct = 31
    Nov = 30
    Dec = 31

    def __init__(self, year):
        # add all
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            # add 1 to Feb
            ...



years = [x for x in range(1900, 2001)]
