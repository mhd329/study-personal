import sys
sys.stdin = open("4948.txt", 'r')

T = True

while T:
    p = set()
    n = int(sys.stdin.readline())
    sqrt_ = int((2 * n) ** 0.5) + 1
    
    for i in range(n + 1, (2 * n) + 1):
        for j in range(2, sqrt_):
            if not i % j:
                break
        else:
            p.add(i)
            
    if not n:
        T = False
    else:
        print(len(p))