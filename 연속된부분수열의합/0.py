def solution(seq, k):
    l = len(seq)
    total = [0] * (l + 1)
    answer = []
    p2 = 0
    for i in range(1, l + 1):
        total[i] = total[i - 1] + seq[i - 1]
    for p1 in range(l + 1):
        end = l
        while p2 < end and total[p2] - total[p1] < k:
            p2 += 1
        if p2 <= end and total[p2] - total[p1] == k:
            answer.append((p2 - p1, [p1, p2 - 1]))
    answer.sort(key = lambda x: x[0])
    return answer[0][1]