import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
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

# 어떤 리스트를 만들고 그 리스트 안에 0부터 9까지
# 없으면 추가, 있으면 패스
# 매 회마다, 리스트의 요소 검사해서 리스트안에 다 있으면 종료 후 출력