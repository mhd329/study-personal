import sys
sys.stdin = open("11650.txt", 'r')
N = int(sys.stdin.readline())
arr = []
d = {}
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x not in d:
        d[x] = []
        d[x].append(y)
    else:
        d[x].append(y)
for i in d.items():
    arr.append(i)
arr.sort()
for j in arr:
    j[1].sort()
    for k in j[1]:
        print(j[0], k)