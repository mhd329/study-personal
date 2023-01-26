import sys
sys.stdin = open("2108.txt", 'r')
N = int(sys.stdin.readline())
s = 0
d = {}
arr = []
for _ in range(N):
    n = int(sys.stdin.readline())
    s += n
    arr.append(n)
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
arr.sort()
print(round(s / N))
print(arr[N // 2])
q = []
for k, v in d.items():
    if len(q):
        if v > q[-1][1]:
            q.clear()
            q.append([k, v])
        elif v < q[-1][1]:
            pass
        else:
            q.append([k, v])
    else:
        q.append([k, v])
q.sort()
if len(q) >= 2:
    print(q[1][0])
else:
    print(q[0][0])
print(abs(arr[-1] - arr[0]))

# 더 짧은 코드

'''
import sys
N=int(input())
nums=[0]*8001
lst=[]
for i in range(N):
    n=int(sys.stdin.readline())
    nums[4000+n]+=1
    lst.append(n)
print(round(sum(lst)/N))
print(sorted(lst)[N//2])
mval=max(nums)
n_list=list(filter(lambda x:nums[x]==mval,range(8001)))
if len(n_list)==1:
    print(n_list[0]-4000)
else:
    print(sorted(n_list)[1]-4000)

print(max(lst)-min(lst))
'''