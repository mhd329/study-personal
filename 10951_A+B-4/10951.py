import sys
sys.stdin = open("10951.txt", 'r')

while 1:
    try:
        A, B = map(int, input().split())
        print(A + B)
    except:
        break
