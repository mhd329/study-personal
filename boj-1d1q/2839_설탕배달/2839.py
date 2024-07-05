import sys
sys.stdin = open("2839.txt", 'r')

N = int(sys.stdin.readline())

i = (N // 5) # 기준 봉지 수

if N < 5 and N != 3: # 이 경우는 무조건 안되는 경우
    print(-1)
else:
    if N % 5: # 5 에 담고 남는 설탕
        while 1:
            if (N - (5 * i)) % 3: # 남은 설탕을 3 에 담았는데도 남은 경우
                i -= 1 # 5 봉지를 한개씩 빼주면서 다시 계산
                if i == -1: # 봉지가 결국 다 빠지면서 -1 봉지가 되는 경우
                    print(i)
                    break
            else:
                print(i + ((N - (5 * i)) // 3)) # 남은 설탕을 3 에 담았을때 맞아 떨어지는 경우
                break
    else:
        print(N // 5)
