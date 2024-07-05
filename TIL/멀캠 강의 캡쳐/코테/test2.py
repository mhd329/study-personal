def solution(name):
    answer = 0
    first_A = 0
    cnt_list = []
    for s in name:
        cnt_list.append(ord(s) - ord('A') if ord(s) - ord('A') < ord('Z')+1 - ord(s) else ord('Z')+1 - ord(s))
    print(cnt_list)
    ltr = len(name) - 1
    
    return answer

solution("JAZA")