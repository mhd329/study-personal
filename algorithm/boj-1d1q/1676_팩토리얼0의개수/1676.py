N = int(input())
if N:
    for i in range(N - 1, 1, -1):
        N *= i
    N = str(N)[::-1]
    cnt = 0
    for i in N:
        if not int(i):
            cnt += 1
        else:
            break
    print(cnt)
else:
    print(0)

# 다른 사람은 아래와 같이 풀었다.

"""
n = int(input())
def five_count(n):
    cnt = 0
    while n != 0:
        n //= 5
        cnt += n
    return cnt
    
print(five_count(n))
"""
