import sys

N = int(sys.stdin.readline())
cards = []
throw = []

for i in range(1, N + 1):
    cards.append(i)

while len(cards) > 1:
    throw.append(cards.pop(0))
    cards.append(cards.pop(0))

for j in throw:
    print(j, end=" ")
else:
    print(*cards)
