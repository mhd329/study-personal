import sys
sys.stdin = open("10989.txt", 'r')

N = int(sys.stdin.readline())
t = [0] * 10001

for _ in range(N):
    n = int(sys.stdin.readline())
    t[n] += 1

for i in range(1, 10001):
    j = 0
    while j < t[i]:
        print(i)
        j += 1