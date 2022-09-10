import sys
sys.stdin = open("1213.txt", 'r')

s = sys.stdin.readline().rstrip()

s = sorted(s)
cnt = {}

for alp in s:
    if alp in cnt:
        cnt[alp] += 1
    else:
        cnt[alp] = 1

center = []
side = []

for i in cnt:
    if not cnt[i] % 2:
        for _ in range(cnt[i] // 2):
            side.append(i)
    else:
        if cnt[i] == 1:
            center.append(i)
        else:
            for _ in range(cnt[i] // 2):
                side.append(i)
            center.append(i)

if len(center) > 1:
    print("I'm Sorry Hansoo")
else:
    print(''.join(side + center + side[::-1]))