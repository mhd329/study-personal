N = int(input())
M = [*map(int, input().split())]
cnt = 0
for i in M:
    n = int(i**0.5)
    if n > 1:
        for j in range(n, i):
            if not i % j:
                break
        else:
            cnt += 1
    else:
        cnt += 1 if i != 1 else 0
print(cnt)
