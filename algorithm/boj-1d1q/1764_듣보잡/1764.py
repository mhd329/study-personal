import sys
sys.stdin = open("1764.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

ns = set()
nh = set()

for _ in range(N):
    ns.add(sys.stdin.readline().rstrip())

for _ in range(M):
    nh.add(sys.stdin.readline().rstrip())
    
a = list(ns & nh)
a.sort()
print(len(a))
for i in a:
    print(i)