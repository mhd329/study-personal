import sys
sys.stdin = open("10817.txt", "r")

n = list(map(int, sys.stdin.readline().split()))

n.sort()

print(n[-2])