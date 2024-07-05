n = [*map(int, input().split())]
others = sum(n) - max(n)
if others <= max(n):
    m = others - 1
    print(others + m)
else:
    print(sum(n))
