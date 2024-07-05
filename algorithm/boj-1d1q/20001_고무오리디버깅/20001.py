q_stack = []

while True:
    s = input()
    if s == "고무오리 디버깅 끝":
        if q_stack:
            print("힝구")
            break
        else:
            print("고무오리야 사랑해")
            break
    else:
        if s == "문제":
            q_stack.append(s)
        elif s == "고무오리":
            if q_stack:
                q_stack.pop()
            else:
                q_stack.append("문제")
                q_stack.append("문제")