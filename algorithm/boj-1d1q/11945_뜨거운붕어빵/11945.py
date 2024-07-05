import sys
sys.stdin = open("11945.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

fish = []

for _ in range(N):
    fish.append(sys.stdin.readline().rstrip())

for i in fish:
    print(i[::-1])

# 제출하고 보니까
'''
for _ in range(N):
    fish = (sys.stdin.readline().rstrip())
    print(fish[::-1])
'''
# 로 간단하게 낼 수도 있었다.