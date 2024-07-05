import sys
sys.stdin = open("9012.txt", "r")
T = int(sys.stdin.readline())
for _ in range(T):
    S = sys.stdin.readline().strip()
    cnt = 0
    for s in S[::-1]:
        if s == ")":
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            print("NO")
            break
    else:
        if cnt == 0:
            print("YES")
        else:
            print("NO")