n = 1
ans = [i for i in range(10001)]
while n < 10001:
    j = list(str(n))
    res = sum(map(int, j)) + n
    if res < 10001:
        ans[res] = 0
    n += 1
for n in ans:
    if n:
        print(n)