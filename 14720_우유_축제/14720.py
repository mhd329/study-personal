import sys

sys.stdin = open("14720.txt", 'r')

N = int(sys.stdin.readline())
milk = [*map(int, sys.stdin.readline().split())]

cnt = 1

for i in range(N):
    if milk[i] == 0:
        flavor = milk[i]
        j = i
        break

for k in range(j, N):
    if flavor == 2:
        if milk[k] == 0:
            cnt += 1
            flavor = milk[k]
    else:
        if milk[k] == flavor + 1:
            cnt += 1
            flavor = milk[k]

print(cnt)