# 11729 하노이 탑 이동 순서 문제와 완전히 똑같은 문제이다.

N = int(input())

def move(a, c):
    print(a, c)

def hanoi(disk_num, a, b, c):
    if disk_num == 1:
        move(a, c)
    else:
        hanoi(disk_num - 1, a, c, b)
        move(a, c)
        hanoi(disk_num - 1, b, a, c)

print((2 ** N) - 1)
if N <= 20:
    hanoi(N, '1', '2', '3')