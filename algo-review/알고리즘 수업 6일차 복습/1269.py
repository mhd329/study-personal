import sys

sys.stdin = open("1269.txt", "r")

A, B = map(int, sys.stdin.readline().split())

a = set([*map(int, sys.stdin.readline().split())])
b = set([*map(int, sys.stdin.readline().split())])

print(len(a - b) + len(b - a))