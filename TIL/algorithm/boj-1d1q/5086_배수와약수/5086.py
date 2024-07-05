import sys
sys.stdin = open("5086.txt", 'r')

class MultiplesAndDivisors:
    def __init__(self):
        self.n = 0
        self.m = 0
    
    @property
    def answer(self):
        return self.__ans
    
    @answer.setter
    def answer(self, value):
        self.__n = value[0]
        self.__m = value[1]
        self.__ans = self.calculate()
    
    def calculate(self):
        self.a = self.__n % self.__m
        self.b = self.__m % self.__n
        if self.a and self.b:
            return "neither"
        elif self.a > self.b:
            return "factor"
        elif self.a < self.b:
            return "multiple"

while 1:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    res = MultiplesAndDivisors()
    res.answer = N, M
    print(res.answer)