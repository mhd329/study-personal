import sys
sys.stdin = open("10871.txt", 'r')

N, X = map(int, input().split())
numbers = list(map(int, input().split()))

for i in numbers:
    if i < X:
        print(i, end = ' ')