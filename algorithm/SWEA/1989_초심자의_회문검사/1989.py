# 어떤 문자열의 절반을 나눈 다음
# 그 절반을 뒤집은 값과 나머지 반쪽을 비교해서 같으면 1 다르면 0
# [::-1]을 하면 마지막 글자는 생략되면서 인덱싱

import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
    s = input() # hannah
    front_half = []
    back_half = []
    front_half.append(s[:len(s) // 2])
    if len(s) % 2 == 0:
        back_half.append(s[len(s):(len(s) // 2) - 1:-1])
    else:
        back_half.append(s[len(s):(len(s) // 2):-1])
    back_half.reverse()

    print(f"#{test_case} {int(front_half == back_half)}")