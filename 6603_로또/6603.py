import sys

sys.stdin = open("6603.txt", "r")


def ans(idx, d):
    if d == 7:
        print(*res)
        return 0
    for i in range(idx, t[0] + 1):
        res.append(t[i])
        ans(i + 1, d + 1)
        res.pop()


while 1:
    t = [*map(int, sys.stdin.readline().split())]
    res = []
    if t[0]:
        ans(1, 1)
    else:
        break
    print()