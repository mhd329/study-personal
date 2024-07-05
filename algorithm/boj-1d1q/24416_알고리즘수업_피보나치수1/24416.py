N = int(input())
cnt_1 = 0
cnt_2 = 0

def fib(n):
    if n == 1 or n == 2:
        global cnt_1
        cnt_1 += 1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

f = []
for i in range(N + 1):
    f.append(0)

def fibonacci(n):
    global cnt_2
    f[1] = f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        cnt_2 += 1
    return f[n]

fib(N)
fibonacci(N)

print(cnt_1, cnt_2)

# 다른 풀이
# 굳이 global 을 안씀

'''
def fin(n):
    if n==1 or n==2:
        return 1
    else:
        return fin(n-1)+fin(n-2)

def finb(n):
    dp = [0]*(n+1)
    dp[1],dp[2] = 1,1
    cnt = 0
    for i in range(3,n+1):
        dp[i] = dp[i-2]+dp[i-1]
        cnt+=1
    return cnt

n = int(input())
print(fin(n),finb(n))
'''

# 아주 짧은 풀이

'''
n = int(input())
f = [1, 1]
for i in range(2, n):
    f.append(f[i - 1] + f[i - 2])
print(f[n - 1], max(0, n - 2))
'''