a, b = input().split() # 734 893

if int(a[::-1]) > int(b[::-1]): # 거꾸로 읽어온 값을 정수화 시켜서 크기를 비교한 다음 조건문에 따라 출력한다.
    print(int(a[::-1]))
else:
    print(int(b[::-1]))