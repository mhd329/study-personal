import sys
sys.stdin = open("1100_하얀칸.txt", 'r')

cnt = 0
for i in range(8):
    cnt += sys.stdin.readline().rstrip()[i % 2::2].count('F')

print(cnt)