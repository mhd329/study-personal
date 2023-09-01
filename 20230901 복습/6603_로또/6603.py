import sys

sys.stdin = open("6603.txt", "r")


def ans(idx):
    if idx == 6:
        print(t[idx])
        print()
        return
    for i in range(idx, t[0]):
        print(t[i], end=" ")
        ans(t[i + 1])


while 1:
    t = [*map(int, sys.stdin.readline().split())]
    if t[0]:
        for i in range(1, t[0]):  # 1 ~ 7
            ans(i)
    else:
        break