import sys
sys.stdin = open("4344.txt", 'r')

T = int(input())

for test_case in range(1, T + 1):
    score_list = [*map(int, input().split())]
    cnt = 0
    for students_score in score_list[1:]:
        if students_score > sum(score_list[1:]) / (score_list[0]):
            cnt += 1
    print(f"{cnt / score_list[0] * 100:.3f}%")