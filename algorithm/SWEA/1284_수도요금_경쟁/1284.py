import sys
sys.stdin = open("input.txt", 'r')

t = int(input())
'''
이것은 이전버전
줄여보겠다는 생각에 조건문을 통으로 만들었지만,
가독성이 너무 떨어지게 되었다.
for test_case in range(1, t + 1):
    p, q, r, s, w = list(map(int, input().split()))
    
    res = p * w if\
                    (q + s * (w - r) if w > r else q) > p * w\
                                                                else q + s * (w - r)\
                                                                                        if w > r else q
    print(f"#{test_case} {res}")
'''
# 다른 사람들은 Q + S * (W - R) 만 가지고 풀었다.
# 그러면 if 를 저렇게 복잡하게 쓸 필요가 없다.
# 강사님은 min 내장함수로 더 깔끔하게 짰다.

for test_case in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    
    a = p * w
        
    if w > r:
        b = q + s * (w - r)
    else:
        b = q
    
    print(f"#{test_case} {a if a < b else b}") # 혹은 min(a, b)