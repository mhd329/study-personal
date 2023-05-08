def solution(msg):
    answer = []
    d = {}
    idx = 26
    for i in range(1, 27):
        d[chr(64 + i)] = i
    # 최대 길이부터 시작하여 줄여가면서 탐색?
    l = len(msg)
    i = 0
    while i < l:
        j = l
        s = msg[i:j]
        while 1:
            if s in d:
                answer.append(d[s])
                idx += 1
                d[msg[i:j + 1]] = idx
                i = j
                break
            j -= 1
            s = msg[i:j]
    
    return answer


print(solution("KAKAO"))