import sys
sys.stdin = open("10828.txt", 'r')
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    command = sys.stdin.readline()
    if "push" in command:
        stack.append(command.split()[1])
    if "pop" in command:
        try:
            print(stack.pop())
        except:
            print(-1)
    if "size" in command:
        print(len(stack))
    if "empty" in command:
        if len(stack):
            print(0)
        else:
            print(1)
    if "top" in command:
        try:
            print(stack[-1])
        except:
            print(-1)