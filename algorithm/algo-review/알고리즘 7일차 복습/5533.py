import sys
sys.stdin = open("5533.txt", 'r')

N = int(sys.stdin.readline())
scoreSET = []
player = [0] * N

for _ in range(N):
    score = [*map(int, sys.stdin.readline().split())]
    scoreSET.append(score)

for i in range(3):
    for j in range(N):
        other_player = 0
        my_score = scoreSET[j][i]
        while other_player < len(player):
            if j != other_player and my_score == scoreSET[other_player][i]:
                my_score = 0
                break
            other_player += 1
        player[j] += my_score

for k in player:
    print(k)