import sys
sys.stdin = open("11651.txt", 'r')
N = int(sys.stdin.readline())
seq = []
for _ in range(N):
    seq.append([*map(int, sys.stdin.readline().split())])
seq.sort()
seq.sort(key=lambda x:x[1])
for i in seq:
    print(*i)