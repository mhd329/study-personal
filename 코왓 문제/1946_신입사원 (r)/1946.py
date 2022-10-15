import sys
sys.stdin = open("1946.txt", 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    A = []
    for _ in range(N):
        A.append(tuple(map(int, sys.stdin.readline().split())))
    A.sort()
    p = 1
    r = A[0][1]
    for a in A:
        if r > a[1]:
            r = a[1]
            p += 1
    print(p)