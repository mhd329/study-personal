p = 1, 1, 2, 2, 2, 8
r = [*map(int, input().split())]
print(*[x - y for x, y in zip(p, r)])