p, k = map(int, (input().split()))
cnt = 0

while p >= k:
    k += 1
    cnt += 1
    
print(cnt)