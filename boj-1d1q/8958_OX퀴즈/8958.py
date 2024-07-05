t = int(input())

for test_case in range(1, t + 1):
    s = input()
    score = 0 # 전체 점수 담을 변수를 초기화
    o_cnt = 0 # 정답일 때마다 1씩 누적되며 올라가는 콤보 보너스
    for char in s:
        if char == 'O': # O O X X O X X O O O
            o_cnt += 1 # 콤보가 누적될수록 올라가는 보너스 점수
            score += o_cnt # 누적되어가는 콤보 보너스를 점수에 더함
        if char == 'X':
            o_cnt = 0 # 오답이 되어 콤보가 끊길 경우 보너스 초기화

    print(score)