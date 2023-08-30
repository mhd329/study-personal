n = []
for _ in range(3):
    n.append(int(input()))
if sum(n) > 180 or sum(n) < 180:
    print("Error")
else:
    m = set(n)
    if len(m) == 1:
        print("Equilateral")
    if len(m) == 2:
        print("Isosceles")
    if len(m) == 3:
        print("Scalene")