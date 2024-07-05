import sys
sys.stdin = open("10816.txt", 'r')

N = int(input())

my_cards = list(map(int, input().split()))
num_of_cards = {}

for card in my_cards:
    if card in num_of_cards:
        num_of_cards[card] += 1
    else:
        num_of_cards[card] = 1

M = int(input())

target = list(map(int, input().split()))

for target_cards in target:
    print(num_of_cards.get(target_cards, 0), end = ' ')