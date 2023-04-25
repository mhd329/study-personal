relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

def solution(relation):
    col_len = len(relation)
    row_len = len(relation[0])
    s = set()
    end = 0
    arr = []
    for start in range(row_len):
        while end < row_len:
            for t in relation:
                if t[start] == t[end]:
                    if t[end] not in s:
                        s.add(t[end])
                    else:
                        break
                else:
                    if (t[start], t[end]) not in s:
                        s.add((t[start], t[end]))
                    else:
                        break
            if len(s) == col_len:
                s.clear()
                if (start, end) not in arr:
                    arr.append((start, end))
                end += 1
                break
            s.clear()
            end += 1
    answer = len(arr)
    return answer

solution(relation)