def solution(friends, gifts):
    
    matrix = [[0 for i in friends] for j in friends]

    l = range(len(friends))
    point = {i: 0 for i in l}
    
    for g in gifts:
        give, receive = g.split()
        g = friends.index(give)
        r = friends.index(receive)
        matrix[g][r] += 1
        point[g] += 1
        point[r] -= 1
    
    res = {i: 0 for i in l}
    
    for g in l:
        for r in l:
            if g == r:
                continue
            if matrix[g][r] > matrix[r][g]:
                res[g] += 1
            elif matrix[g][r] < matrix[r][g]:
                res[r] += 1
            else:
                if point[g] > point[r]:
                    res[g] += 1
                elif point[g] < point[r]:
                    res[r] += 1

    res = max(res.values())
    if res:
        res //= 2
    answer = res
    
    return answer

solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])