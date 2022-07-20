# import sys
# sys.stdin = open("input.txt", 'r')

n = int(input())

for i in range(n + 1):
    print(f"{2 ** i}", end = ' ')