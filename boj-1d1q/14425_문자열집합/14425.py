import sys
sys.stdin = open("14425.txt", 'r')
N, M = map(int, sys.stdin.readline().split())
S = set()
cnt = 0
for _ in range(N):
    S.add(sys.stdin.readline().strip())
for _ in range(M):
    if sys.stdin.readline().strip() in S:
        cnt += 1
print(cnt)