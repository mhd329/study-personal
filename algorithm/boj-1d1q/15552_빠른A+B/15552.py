import sys

sys.stdin = open("15552.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
    
    n = map(int, sys.stdin.readline().split())
    print(sum(n))