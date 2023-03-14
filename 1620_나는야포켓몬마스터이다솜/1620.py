import sys
sys.stdin = open("1620.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
pokemon = {}
for _ in range(N):
    
    if pokemon