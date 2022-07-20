import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
    p, q, r, s, w = list(map(int, input().split()))
    
    res = p * w if\
                    (q + s * (w - r) if w > r else q) > p * w\
                                                                else q + s * (w - r)\
                                                                                        if w > r else q
    print(f"#{test_case} {res}")