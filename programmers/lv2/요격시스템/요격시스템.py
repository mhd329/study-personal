def solution(targets):
    answer = 0
    targets.sort(key = lambda x: [x[1], x[0]])
    target_end = 0
    for target in targets:
        target_start = target[0]
        if target_start >= target_end:
            answer += 1
            target_end = target[1]
    return targets