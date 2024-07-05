## 전역변수 a, b, c, d, e 가 각각 있음 
## 매 업데이트 시마다 각 변수는 다음의 값으로 업데이트 됨 
## a : 1씩 증가  
## b : 2배로 증가 
## c : 10배한 후 d를 더함 
## d : d가 짝수이면 2로 나누고, 홀수이면 3을 곱한 후 1을 더한다.  
## e : 제곱이 된다. 

a = 10
b = 10
c = 10
d = 10
e = 10

def update_global_values():    
  return (a + 1,
          b * 2,             
          c * 10 + d,
          d // 2 if d % 2 == 0 else d * 3 + 1,  
          e * e) 

## 업데이트된 값을 구하는 함수는 규칙에 맞게 계산된 값을 튜플로 리턴하고,  
## 실제 업데이트는 아래와 같이 루트 레벨에서 직접 대입한다.  
update_global_values() # 이 호출에서는 실제로 업데이트 되는 값이 없다. 

a, b, c, d, e = update_global_values()

print(a)
print(b)
print(c)
print(d)
print(e)

print("-----------------------------------")

print("나쁜 경우")

a = 0
b = 1

def AAA():
    print(a)
    print(b)

AAA()

print("-----------------------------------")

print("올바른 경우")

c = 2
d = 3

def BBB(xx, yy):
    print(xx)
    print(yy)

BBB(c, d)