'''
N = input()
n = []
for i in N:
    n.append(i)
n.sort(reverse=1)
n = ''.join(n)
print(n)
'''
# 나는 위의 코드로 적당히 풀었지만 코드가 긴 사람이 있어서 코드를 보니 그 사람은 합병정렬로 풀어냈다.
# 합병정렬로 풀어보기
N = input()
arr = []
for _ in N:
    arr.append(_)

def merge(ans1, ans2):
    res = []
    while ans1 and ans2:
        if ans1[0] < ans2[0]:
            res.append(ans2.pop(0))
        else:
            res.append(ans1.pop(0))
    res += ans1 if ans1 else ans2
    return res

def div(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    front = arr[:mid]
    back = arr[mid:]
    
    res1 = div(front)
    res2 = div(back)
    
    return merge(res1, res2)
ans = ''.join(div(arr))
print(ans)