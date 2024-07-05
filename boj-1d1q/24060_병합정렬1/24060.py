'''
import sys
sys.stdin = open("24060.txt", 'r')
A, K = map(int, sys.stdin.readline().split())
arr = [*map(int, sys.stdin.readline().split())]
def merge(front, back, answer):
    res = []
    while front and back:
        if front[0] > back[0]:
            a = back.pop(0)
            res.append(a)
            answer.append(a)
        else:
            b = front.pop(0)
            res.append(b)
            answer.append(b)
    res += front if front else back
    answer += front if front else back
    return res, answer
def div(arr, answer):
    if len(arr) == 1:
        return arr, answer
    mid = (len(arr) + 1) // 2
    front = arr[:mid]
    back = arr[mid:]
    front, answer = div(front, answer)
    back, temp = div(back, answer)
    return merge(front, back, temp)
answer = div(arr, [])[1]
if K > len(answer):
    print(-1)
else:
    print(answer[K - 1])
'''
import sys
import itertools
import collections
sys.stdin = open("24060.txt", 'r')
A, K = map(int, sys.stdin.readline().split())
arr = collections.deque([*map(int, sys.stdin.readline().split())])
def merge(front, back):
    res = collections.deque()
    while front and back:
        if front[0] > back[0]:
            a = back.popleft()
            res.append(a)
            answer.append(a)
        else:
            b = front.popleft()
            res.append(b)
            answer.append(b)
    while front:
        a = front.popleft()
        res.append(a)
        answer.append(a)
    while back:
        b = back.popleft()
        res.append(b)
        answer.append(b)
    return res
def div(arr):
    if len(arr) == 1:
        return arr
    mid = (len(arr) + 1) // 2
    front = collections.deque(itertools.islice(arr, 0, mid))
    back = collections.deque(itertools.islice(arr, mid, len(arr)))
    front = div(front)
    back = div(back)
    return merge(front, back)
answer = collections.deque()
div(arr)
if K > len(answer):
    print(-1)
else:
    print(answer[K - 1])

# 배운점

# 1. pop(0) 은 리스트가 길어질수록 엄청나게 시간이 오래걸린다.
# 왜냐하면 맨 앞의 원소를 빼면 그 뒤의 모든 원소들이 차례로 앞으로 이동하면서 리스트가 수정되기 때문이다.
# 참고 : https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%98-listpop0%EC%9D%84-%EC%93%B0%EB%A9%B4-%EC%95%88-%EB%90%98%EB%82%98%EC%9A%94

# 2. 함수 바깥에서 변수를 선언한 수 그것을 함수 내부에서 사용할 때 함수 내부에서 다시 재선언 해버리면 먼저 참조되었다면서 사용할 수 없게 된다.
# 이것은 당연히 알고 있었지만 가령 이런식으로 했을 때,
# >>> answer += front if front else back
# += 연산자가 answer 를 한번 변수로 할당해주는거라 자꾸 먼저 참조되었다고 하면서 안되었다.
# 기본적인 것인데 까먹어서 자꾸 실수했음