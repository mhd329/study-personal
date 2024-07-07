import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
    h1, m1, h2, m2 = map(int, input().split())
    
    h3 = h1 + h2 # 시 합산
    
    m3 = m1 + m2 # 분 합산
    
    if h3 > 12:
        h3 -= 12
    
    if m3 > 59:
        h3 += 1
        m3 -= 60
        
    print(f"#{test_case} {h3} {m3}")