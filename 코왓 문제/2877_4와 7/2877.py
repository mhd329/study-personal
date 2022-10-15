K = int(input())
n = 0
while 1:
    i = (2 ** n) - 1
    j = (2 ** (n + 1)) - 2
    if i <= K and K <= j:
        # 그런데 i + 1 의 앞자리는 필요가 없으니 리스트 슬라이싱을 해서 리플레이스 해주는 아래의 식을 사용하면 목표하는 정답이 나온다.
        print(bin((i + 1) + K - i)[3:].replace("0", "4").replace("1", "7"))
        break
    n += 1