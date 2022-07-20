<br>

```python
try:
    어쩌구 저쩌구
except: # 만약 예외가 발생하면
    '에러입니다 !!' # 해당 메세지를 출력
```
<br>
```python
try:
    어쩌구 저쩌구
except ValueError, ZeroDivisionError: # 두 가지 이상의 예외를 합쳐서 처리할 수 있다.
    '에러에러에러'
```
<br>
```python
try:
    어쩌구 저쩌구
except ZeroDivisionError as err:
    print(err) # 원래의 ZeroDivisionError 메세지에 내가 추가로 코멘트 할 수 있다.
    '에러입니다 !!'
```
<br>