import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

def test_case(t):
    for i in range(1, t + 1):
        a, b = map(int, input().split())
        print(f"#{i}" ,a//b, a % b)
        
test_case(t)