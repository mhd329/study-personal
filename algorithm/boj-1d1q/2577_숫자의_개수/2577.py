a = int(input())
b = int(input())
c = int(input())

multiply = a * b * c
result_dict = {}

for i in range(10): # 0 부터 9 까지 딕셔너리 키 만듦
    result_dict[str(i)] = 0 # 곱셈 결과를 문자열로 바꾼 다음 처음부터 끝까지 인덱싱 할 것이기 때문에 그에 맞게 딕셔너리의 각 키도 문자열로 바꿔줘야 한다.
    
for j in str(multiply): # 17037300
    if j in result_dict: # 여기서 j 는 문자이다.
        result_dict[j] += 1
    else:
        result_dict[j] = 1

for k in result_dict.values():
    print(k)