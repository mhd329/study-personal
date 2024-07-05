class Car:
    """
    Car class
    Author: 현동
    Date: 2023.09.08
    """

    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 매직 메서드
    def __str__(self):
        return "str: {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)

    def detail_info(self):
        print("Current ID: {}".format(id(self)))
        print(
            "Car Detail Info: {} {}".format(self._company, self._details.get("price"))
        )


car1 = Car("Kia", {"color": "White", "hp": 130, "price": 3000})
car2 = Car("Hyundai", {"color": "Silver", "hp": 160, "price": 5000})
car3 = Car("GM", {"color": "Black", "hp": 190, "price": 7000})

# ID 확인

# print(id(car1))
# print(id(car2))
# print(id(car3))

# print(car1._company == car2._company)
# print(car1 is car2)

# dir & __dict__ 확인

# print(dir(car1))
# print(dir(car2))

# print(car1.__dict__)
# print(car2.__dict__)

# Docstring
# print(Car.__doc__)

# car1.detail_info()
# print()
# car2.detail_info()

# 비교

print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car2.__class__) == id(car3.__class__))
