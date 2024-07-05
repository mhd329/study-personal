import sys
sys.stdin = open("10988.txt", 'r')
s = sys.stdin.readline().strip()
l = len(s) - 1
def palindrome(front:int, rear:int, s:str) -> bool:
    if front >= rear:
        return 1
    if s[front] == s[rear]:
        ans = palindrome(front + 1, rear - 1, s)
        return ans
    else:
        return 0
print(palindrome(0, l, s))