import sys
sys.stdin = open("2920.txt", 'r')

N = [*map(int, sys.stdin.readline().split())]

if N == sorted(N):
    print("ascending")
elif N == sorted(N, reverse = True):
    print("descending")
else:
    print("mixed")