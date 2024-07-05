import sys
n = int(sys.stdin.readline())
a = 1
b = 1
while 1:
    if a >= n:
        break
    a += b + 1
    b += 1

if b % 2 == 0:
    numerator = b - (a - n)
    denominator = 1 + (a - n)
else:
    numerator = 1 + (a - n)
    denominator = b - (a - n)

print(f"{numerator}/{denominator}")