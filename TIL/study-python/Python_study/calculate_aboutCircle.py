import math

class circle:
    # 객체를 만들 때 반지름 설정
    def __init__(self):
        self.__radius = int(input("계산할 값 입력 : "))
        self.radius
        self.calculate_circumference()
        self.calculate_area()
        self.result()
    # 객체는 어떤 반지름 값을 가지고 만들어짐 = 반지름 값 고정
    # 이미 만들어진 객체의 반지름 값을 바꾸고 싶을때 setter, getter
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, radius):
        if radius < 0:
            print("*** 반지름이 음수입니다. ***")
            self.__radius = radius
        else:
            self.__radius = radius
            
    def calculate_circumference(self):
        return 2 * math.pi * self.radius
    
    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
    def result(self):
        print(f"원 둘레 : {self.calculate_circumference():.3f}")
        print(f"원 넓이 : {self.calculate_area():.3f}")
        
Circle1 = circle()
print("*" * 80)
Circle1.radius = int(input("새로 설정할 값 : "))
Circle1.result()
print("*" * 80)