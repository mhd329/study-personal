import sys
sys.stdin = open("input.txt", 'r')

t = int(input())
# 이것은 줄인버전
# 불필요한 계산을 줄였다.
# 일부러 set 을 사용하는 방법은 사용하지 않았다.
for test_case in range(1, t + 1):
    n = int(input())
    m = n
    numbers = []
    cnt = 0

    while len(numbers) < 10:
        for i in str(n): # 1
            if i not in numbers:
                numbers.append(i)
        n += m
        cnt += 1
        
    print(f"#{test_case} {m * cnt}")

# 어떤 리스트를 만들고 그 리스트 안에 0부터 9까지
# 없으면 추가, 있으면 패스
# 매 회마다, 리스트의 요소 검사해서 리스트안에 다 있으면 종료 후 출력

'''
이것은 이전버전
불필요한 계산이 많다.
n = input()
    numbers = []
    cnt = 0
    m = int(n)
    multiple = 1

    while len(numbers) < 10:
        for i in n: # 1
            if i not in numbers:
                numbers.append(i)
        multiple += 1
        n = int(n)
        n = m * multiple
        n = str(n)
        cnt += 1
        
    print(f"#{test_case} {m * cnt}")
'''