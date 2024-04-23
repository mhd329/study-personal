import sys
sys.stdin = open("2798.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
cards = [*map(int, sys.stdin.readline().split())]
m = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if M >= cards[i] + cards[j] + cards[k] > m:
                m = cards[i] + cards[j] + cards[k]
print(m)