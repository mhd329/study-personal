while 1:
    n = [*map(int, input().split())]
    if not sum(n):
        break
    if sum(n) - max(n) <= max(n):
        print("Invalid")
        continue
    m = set(n)
    if len(m) == 1:
        print("Equilateral")
    if len(m) == 2:
        print("Isosceles")
    if len(m) == 3:
        print("Scalene")