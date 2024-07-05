class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    # 매직 메서드
    def __str__(self):
        return "str: {} - {}".format(self._company, self._details)

    def __repr__(self):
        return "repr: {} - {}".format(self._company, self._details)


some_car = Car("Kia", {"color": "white", "hp": 160, "price": 3000})

car_list = [some_car]

print(car_list)
