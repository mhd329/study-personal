import sys

sys.stdin = open("1026.txt", "r")
N = int(sys.stdin.readline())
A = [*map(int, sys.stdin.readline().split())]
B = [*map(int, sys.stdin.readline().split())]
A.sort()
B.sort(reverse=True)
total = 0
for i in range(N):
    total += A[i] * B[i]
print(total)
