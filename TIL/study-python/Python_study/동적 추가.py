# 오류 발생
class sample:
    def __init__(self):
        self.data += 100

a = sample()
print(a.data)

# 클래스 변수 동적 추가
class sample:
    def __init__(self):
        self.data += 100

sample.data = 0

a = sample()
print(a.data)