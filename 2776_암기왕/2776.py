import sys
sys.stdin = open("2776.txt", 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    N = int(sys.stdin.readline())
    nums_n = [*map(int, sys.stdin.readline().split())]
    M = int(sys.stdin.readline())
    nums_m = [*map(int, sys.stdin.readline().split())]
    num_m_set = set(nums_m)
    
    false_num = (set(nums_n) ^ num_m_set) & num_m_set
    
    for num in nums_m:
        if num in false_num:
            print(0)
        else:
            print(1)