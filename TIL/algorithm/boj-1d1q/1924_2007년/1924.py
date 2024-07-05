'''
import calendar

x, y = map(int, input().split())
d = calendar.weekday(2007, x, y)

if d == 0:
    print("MON")
if d == 1:
    print("TUE")
if d == 2:
    print("WED")
if d == 3:
    print("THU")
if d == 4:
    print("FRI")
if d == 5:
    print("SAT")
if d == 6:
    print("SUN")
'''
x, y = map(int, input().split())

month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
day = ("SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT")

d = 0
for m in range(0, x):
    d += month[m]
else:
    d += y

print(day[d % 7])