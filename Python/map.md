# map()에 대한 공부 이것저것.

<br>

알고리즘 문제를 풀다가 map을 쓸 일이 생겼다.

상황은 이러하다.

 

1. list1 에 있는 내부 요소들을 list2 로 옮겨야 된다.

2. 방법이야 여러 가지가 있겠지만, map을 써서 옮길 수 없을까 생각했다.

3. append 함수가 있으니, map을 활용해서 해볼 수 있겠다 생각함.

4. 여러 가지 버전의 코드들을 테스트 해봤다.

---

```
# 1
list1 = [1, 2, 3]

list2 = []

list2 = [*map(list2.append, list1)]

print(list2) # [None, None, None]

# 2
list1 = [1, 2, 3]

list2 = []

map(list2.append, list1)

print(list2) # []

# 3
list1 = [1, 2, 3]

list2 = []

[map(list2.append, list1)]

print(list2) # []

# 4
list1 = [1, 2, 3]

list2 = []

[*map(list2.append, list1)]

print(list2) # [1, 2, 3]
```

---

\# 1 의 경우

append 함수는 추가하는 동작만 하고 None을 반환한다. 따라서 map이 생성한 이터러블 객체들은 모두 None이고 list2에 담긴다.

 

\# 2 ~ 4 의 경우

아래 설명 참조.

------

```
list1 = [1, 2, 3]
list2 = []
map(list2.append, list1)
print(list2)
```

 

map함수의 결과값 뭉치, 즉 append가 개별로 동작하면서 그때그때 뱉어내는 반환값들이 필요한 게 아니라 append의 동작만 필요하기 때문에 map함수를 호출만 해줬다.



내 예상은 [1, 2, 3] 이었다.



그런데 결과는 빈 리스트 [] 였다.



왜 그렇지?