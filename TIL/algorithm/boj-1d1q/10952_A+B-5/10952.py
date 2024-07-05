import sys
sys.stdin = open("10952.txt", 'r')

while True:
    A, B = map(int, input().split())
    if A != 0 and B != 0:
        print(A + B)
    else:
        break