import sys
sys.stdin = open("9325.txt", 'r')

T = int(sys.stdin.readline())
for _ in range(T):
    s = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        s += (q * p)
    print(s)