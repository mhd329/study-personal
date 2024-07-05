import sys
sys.stdin = open("25501.txt", 'r')
def 검사(문자열, 앞, 뒤, 횟수):
    횟수 += 1
    if 앞 >= 뒤:
        return print(1, 횟수)
    elif 문자열[앞] != 문자열[뒤]:
        return print(0, 횟수)
    else:
        검사(문자열, 앞 + 1, 뒤 - 1, 횟수)

테스트케이스 = int(sys.stdin.readline())

for _ in range(테스트케이스):
    문자열 = sys.stdin.readline().strip()
    검사(문자열, 0, len(문자열) - 1, 0)