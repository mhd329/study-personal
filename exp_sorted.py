def my_key(string): # 문자열에 관한 함수
     return len(string.strip())
 
# 목표로 하는 리스트
target = ['  cat ', ' tiger ', '    dog', 'snake   ']
print(sorted(target, key = my_key)) # sorted 의 key 는 target 에 대하여 일종의 오름차순 관련 for 문이 내부에서 돌아간다 ???
           #(target[i]) key = my_key(target[i])
                            # return >>> 3,3,5,5
                            
print(sorted(target, key = lambda x : len(x.strip())))
# x 는 target[i] ???