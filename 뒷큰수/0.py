def solution(numbers):
    answer = []
    l = len(numbers)
    arr = [-1] * l
    stack = []
    for i in range(1, l):
        if numbers[i] > numbers[i - 1]:
            arr[i - 1] = numbers[i]
            while stack and numbers[stack[-1]] < numbers[i]:
                arr[stack[-1]] = numbers[i]
                stack.pop()
        else:
            stack.append(i - 1)
    answer = arr
    return answer