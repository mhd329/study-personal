from collections import deque
def solution(n, t, m, p):
    # 0, 1, 10, 11, 100
    # 다음 수 까지 셌을때 그것을(진법변환한 다음) list로 만들고 그 길이가 p부터 시작하면서 m간격만큼 띄워가면서 셌을 때 같거나 길면 answer
    # i를 n으로 나누면서 진법변환
    i = 0
    arr = []
    answer = ''
    a = "ABCDEF"
    while 1:
        q = i
        numbers = deque()
        while 1:
            q, r = divmod(q, n)
            if r >= 10:
                numbers.appendleft(a[r % 10])
            else:
                numbers.appendleft(str(r))
            if not q:
                break
        arr.extend(numbers)
        l = len(arr)
        if l < p or l < m * t:
            i += 1
            continue
        for i in range(p - 1, m * t, m):
            answer += arr[i]
        break
    return answer

print(solution(2, 4, 2, 1))