import sys
sys.stdin = open("25305.txt", 'r')

N, k = map(int, sys.stdin.readline().split())
p = [*map(int, sys.stdin.readline().split())]
p.sort(reverse=1)
print(p[k-1])