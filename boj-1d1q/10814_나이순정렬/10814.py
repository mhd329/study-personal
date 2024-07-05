import sys
sys.stdin = open("10814.txt", 'r')
N = int(sys.stdin.readline())
members = []
for _ in range(N):
    o, n = sys.stdin.readline().split()
    members.append([int(o), n])
members.sort(key=lambda x:x[0])
for _ in members:
    print(*_)