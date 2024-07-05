import sys
sys.stdin = open("11652.txt", 'r')

N = int(sys.stdin.readline())

nums = {}

for i in range(N):
    n = int(sys.stdin.readline())
    if n in nums:
        nums[n] += 1
    else:
        nums[n] = 1

cnt = 0
num = 0

for k, v in nums.items():
    if cnt < v:
        cnt = v
        num = k
    elif cnt == v:
        if num > k:
            num = k

print(num)