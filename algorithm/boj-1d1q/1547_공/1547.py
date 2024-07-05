import sys
sys.stdin = open("1547.txt", 'r')

M = int(sys.stdin.readline())

cups = {"ball_1" : True,
        "ball_2" : False,
        "ball_3" : False}

for _ in range(M):
    X, Y = sys.stdin.readline().split()
    if cups[f"ball_{X}"] != cups[f"ball_{Y}"]:
        cups[f"ball_{X}"] = not(cups[f"ball_{X}"])
        cups[f"ball_{Y}"] = not(cups[f"ball_{Y}"])

i = 1
while 1:
    if cups[f"ball_{i}"]:
        print(i)
        break
    i += 1
    if i > 3:
        print(-1)
        break