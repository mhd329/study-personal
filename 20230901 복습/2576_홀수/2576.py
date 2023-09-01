n = []
for _ in range(7):
    m = int(input())
    if m % 2:
        n.append(m)
if n:
    print(sum(n))
    print(min(n))
else:
    print(-1)