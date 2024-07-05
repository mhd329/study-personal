import sys

sys.stdin = open("9012.txt", "r")

T = int(sys.stdin.readline())


def check(vps):
    stack = []
    if len(vps) % 2:
        return print("NO")
    else:
        while vps:
            right = vps.pop()
            if right == ")":
                stack.append(right)
            else:
                if stack:
                    stack.pop()
                else:
                    return print("NO")
    if stack:
        return print("NO")
    else:
        return print("YES")


for _ in range(T):
    VPS = []
    VPS += sys.stdin.readline().rstrip()
    check(VPS)
