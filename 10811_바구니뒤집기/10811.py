import sys
sys.stdin = open("10811.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
basket = [0] + [i for i in range(1, N + 1)]
for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    temp = basket[j + 1:]