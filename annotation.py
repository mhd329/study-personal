# 달력 주석

import calendar

def annotate(yyyy, mm, dd):
    if calendar.weekday(yyyy, mm, dd) == 5:
        print()
    if (calendar.weekday(yyyy, mm, dd) == 5 and dd == 4):
        print("\t")
    if (calendar.weekday(yyyy, mm, dd) == 5 and dd == 11):
        print("\t")
    if (calendar.weekday(yyyy, mm, dd) == 5 and dd == 18):
        print("\t")
    if (calendar.weekday(yyyy, mm, dd) == 5 and dd == 25):
        print("\t")