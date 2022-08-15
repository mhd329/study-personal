import sys
sys.stdin = open("2839.txt", 'r')

N = int(sys.stdin.readline())

i = (N // 5)

if N < 5 and N != 3:
    print(-1)
else:
    if N % 5:
        while 1:
            if (N - (5 * i)) % 3:
                i -= 1
                if i == -1:
                    print(i)
                    break
            else:
                print(i + ((N - (5 * i)) // 3))
                break
    else:
        print(N // 5)
