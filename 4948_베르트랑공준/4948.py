import sys
sys.stdin = open("4948.txt", 'r')

def pn_extractor(N):
    cnt = 0
    if not n:
        return False
    else:
        for i in range(N + 1, m + 1):
            for j in range(2, sqrt_):
                if not i % j:
                    break
            else:
                cnt += 1
        return cnt
    
while 1:
    n = int(sys.stdin.readline())
    m = 2 * n
    sqrt_ = int(m ** 0.5) + 1
    if pn_extractor(n):
        print(pn_extractor(n))
    else:
        break