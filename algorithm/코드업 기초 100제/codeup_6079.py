n = int(input())
res = 0
for i in range(n):
    if res < n:
        res += i
    else:
        print(i-1)
        break