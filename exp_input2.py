a,b,c = 1,2,3
print(a,b,c)
# 받은 값들을 일단 어떤 임의의 문자열로 저장 ( 콤마로 구분 )
# 1,2,3 뒤에 split(",") 가 생략되어있는 상태인것같다
# 문자열을 분해한 다음 리스트로 만들어서 첫 번째 원소부터 각 원소에 대응하는 값이 할당됨

d,e,f = input().split(",")

print(d,e,f)


# 받은 값들을 일단 문자열로 저장 ( input 이기 때문에 스페이스로 구분되는 상태 )
# 그 다음 split(",") 로 분해시킴
# 각 원소에 할당

h,i,j = input().split() # split 으로 구분자를 지정해줄 수 있네

# 받은 값들을 문자열로 저장
# split() 으로 분해 후 리스트생성
# 각 원소에 할당

print(h,i,j)

### input 함수는 다중 변수 ( a,b,c ) 가 있는 상황에서
# 1. 여러 값을 문자열 형태로 입력받고
# 2. 콤마같은 것이나 split 으로 구분할 수 있으면 그것을 구분자로 하여 분해한 다음
# 3. 그대로 리스트로 만들어서 리스트의 원소 [0~n] 을 각 변수에 갯수에 맞게 할당시킨다 ???

# 3-1. 근데 split 을 안쓰고 콤마를 쓸 경우 만약 각 원소 i 가 정수라면 int 로 바꿔주고 할당시킨다

lst1 = [1,2,3,4]
tu1 = 1,2,3,4
a1,b1,c1,d1 = input().split(",")

print(a1,b1,c1,d1)

# print(lst1.split(","))
# print(tu1.split(","))

