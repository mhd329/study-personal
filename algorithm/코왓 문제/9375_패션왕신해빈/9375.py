import sys
sys.stdin = open("9375.txt", 'r')

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    w = []
    wt = set()
    for _ in range(n):
        w.append(sys.stdin.readline().rstrip().split())
        wt.add(w[-1][1])
    for i in wt:
        
    print(w)