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
    
# 다른 사람들은 Q + S * (W - R) 만 가지고 풀었다.
# 그러면 if 를 저렇게 복잡하게 쓸 필요가 없다.
# 강사님은 min 내장함수로 더 깔끔하게 짰다.

for test_case in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    
    res = p * w if\
                    (q + s * (w - r) if w > r else q) > p * w\
                                                                else q + s * (w - r)\
                                                                                        if w > r else q
    print(f"#{test_case} {res}")
    
    a = p * w
    
    b = q + s * (w - r)