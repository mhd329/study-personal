import sys

sys.stdin = open("13458.txt", "r")
testsites = int(sys.stdin.readline())  # 시험장 수
candidates = [*map(int, sys.stdin.readline().split())]  # 응시자들이 있는 시험장
temp = [*map(int, sys.stdin.readline().split())]
main = temp[0]  # 총감독관, 시험장 당 한명만
sub = temp[1]  # 부감독관, 시험장에 여러명 가능

main_cnt = 0
sub_cnt = 0

for site in range(testsites):
    if candidates[site] > 0:
        candidates[site] -= main
        main_cnt += 1
    if candidates[site] > 0:
        sub_cnt += candidates[site] // sub
        candidates[site] %= sub
    if candidates[site] > 0:
        sub_cnt += 1

print(main_cnt + sub_cnt)