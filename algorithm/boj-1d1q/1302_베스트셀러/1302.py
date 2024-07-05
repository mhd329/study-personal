import sys
sys.stdin = open("1302.txt", 'r')

title_dict = {}

N = int(sys.stdin.readline())

for _ in range(N):
    title = sys.stdin.readline().rstrip()
    if title in title_dict:
        title_dict[title] += 1
    else:
        title_dict[title] = 1

cnt = 0
titles = []

for k, v in title_dict.items():
    if v == max(title_dict.values()):
        titles.append(k)

titles.sort()
print(titles[0])
