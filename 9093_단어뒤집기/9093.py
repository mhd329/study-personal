import sys
sys.stdin = open("9093.txt", 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    s = sys.stdin.readline().split()
    
    for i in s:
        print(i[::-1], end = ' ')
    print()