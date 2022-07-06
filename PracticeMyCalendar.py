# --------------------------------------------------------------------------------------------------

import calendar

# 기존 calendar 모듈은 월/화/수 ... 순서인데 일/월/화 순으로 바꾸면서 동시에 오늘의 날짜에는 대괄호 처리를 하는 기능을 가진 달력으로 수정하고 싶어서 만들었다.
# 그리고 어떤 날짜의 기념일도 밑에 써넣고 싶었다.

import annotation

# 달력의 공휴일 등 주석 부분 import ... ex) 광복절, 3.1절, 생일 ... 추가하기 귀찮은데 어디선가 받아올 수 있으면 좋겠다.
# vsc에서는 나름대로 깔끔하게 나오는데 pycharm 에서는 깔끔한 모양이 안나온다 ... 환경에 관계없이 일정하게 만들 수 있을까 ?

# --------------------------------------------------------------------------------------------------

class My_calendar:

    def __init__(self):

        self.__month_correspond =\
        {
        1 : "January", 2 : "February", 3 : "March",
        4 : "April", 5 : "May", 6 : "June",
        7 : "July", 8 : "August", 9 : "September",
        10 : "October", 11 : "November", 12 : "December"
        }

        self.__yyyy = 0
        self.__mm = 0
        self.__dd = 0
        self.get_yyyy()
        self.get_mm()
        self.get_dd()
        self.set_yyyy_mm_dd()
        self.title()
        self.calendar()

# 굳이 init 에서 모든것을 다 호출해야 하는지 모르겠다 ... 일단 써넣었다.

    def get_yyyy(self):
        return self.__yyyy

    def get_mm(self):
        return self.__mm

    def get_dd(self):
        return self.__dd
# --------------------------------------------------------------------------------------------------
    # 년/월/일 입력 ... 예외처리 연습을 위해 raise 를 써 넣었는데 생각만큼 활용이 쉽지 않았다 ... 조금 더 공부해서 완성도 있게 활용해보자.
# --------------------------------------------------------------------------------------------------
    def set_yyyy_mm_dd(self):

        yyyy = int(input("몇 년도 인가요? : "))
        if yyyy > 2200:
            raise Exception("너무 먼 미래가 입력되었습니다.")
        else :
            self.__yyyy = yyyy

        mm = int(input("몇 월 인가요? : "))
        if mm > 12 or mm < 1:
            raise Exception("올바른 날짜를 입력해주세요.")
        else :
            self.__mm = mm

        dd = int(input("몇 일 인가요? : "))
        if dd > 31 or dd < 1:
            raise Exception("올바른 날짜를 입력해주세요.")
        else :
            self.__dd = dd
            
# --------------------------------------------------------------------------------------------------

# 달력 타이틀부분
# 환경에 관계없이 월과 년도가 날짜부분의 윗칸 정 중앙에 오게 만들고 싶다.
# vsc를 기준으로 대충 모양만 맞췄다.

# --------------------------------------------------------------------------------------------------

    def title(self):
        print("\n")
        print((self.__month_correspond[self.get_mm()] + " " + str(self.get_yyyy())).center(50," "))
        print("\n")
        abbreviation = ["Sun", "Mon", "Tus", "Wed", "Thu", "Fri", "Sat"]
        for i in abbreviation:
            print(i, end="\t")
        print("\n")
        
# --------------------------------------------------------------------------------------------------
    # 달력 날짜부분 출력과 오늘의 날짜를 대괄호 처리
# --------------------------------------------------------------------------------------------------
    def calendar(self):

        (first, last) = calendar.monthrange(self.get_yyyy(), self.get_mm())
        print("\t" * ((first + 1) % 7), end="")

        for i in range(1, last + 1):

            if i == self.get_dd():
                print("[" + str(i) + "]", end="\t")
                annotation.annotate(self.get_yyyy(), self.get_mm(), i)

            else:
                    print(i, end="\t")
                    annotation.annotate(self.get_yyyy(), self.get_mm(), i)

calendar_1 = My_calendar()