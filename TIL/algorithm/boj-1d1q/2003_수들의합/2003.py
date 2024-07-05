import sys
sys.stdin = open("2003.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
A = [*map(int, sys.stdin.readline().split())]
cnt = 0
end = 0
total = 0
for start in range(N):
    while total < M and end < N:
        total += A[end]
        end += 1
    if total == M:
        cnt += 1
    total -= A[start]
print(cnt)