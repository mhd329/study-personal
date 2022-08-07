import sys
sys.stdin = open("9012_괄호.txt", 'r')

N = int(sys.stdin.readline())

for _ in range(N):
    PS = list(sys.stdin.readline().rstrip())
    ref = 1
    stack = []
    
    if len(PS) % 2 != 0 or PS[-1] != ')':
        ref = 0 # 문자열의 길이가 짝수가 아니거나 맨 끝이 닫히는 괄호가 아닐때 거짓
    else:
        for _ in range(len(PS)):
            try:
                if PS[-1] == '(':
                    del PS[-1]
                    del stack[-1]
                else:
                    stack.append(PS.pop())
            except IndexError: # PS[-1] 이 닫히는 괄호이면 stack 에서 그에 맞는 열림 괄호가 있어야 하는데 없는 경우 올바른 괄호가 아님
                ref = 0
                break
    if len(stack) == 0 and ref: # stack 의 길이가 1 이상이면 올바른 괄호가 아님
        print("YES")
    else:
        print("NO")