N = int(input())

cnt = 0
sq = []

def move(a, c):
    global cnt
    cnt += 1
    sq.append((a, c))

def hanoi(disk_num, a, b, c):
    if disk_num == 1:
        move(a, c)
    else:
        hanoi(disk_num - 1, a, c, b)
        move(a, c)
        hanoi(disk_num - 1, b, a, c)

hanoi(N, '1', '2', '3')

print(cnt)
for i in sq:
    print(*i, end = '\n')