'''
class Test:
    number = 0
    
    def __init__(self):
        Test.number += 1
        self.name = str(Test.number) + " instance"

if __name__ == "__main__":
    a = Test()
    b = Test()
    c = Test()
    d = Test()

print(a.name)
print(b.name)
print(c.name)
print(d.name)
print(a.name)
print(d.name)
'''

class Test:
    number = 0
    
    def __init__(self):
        self.number += 1
        self.name = str(self.number) + " instance"

if __name__ == "__main__":
    a = Test()
    b = Test()
    c = Test()
    d = Test()

print(a.name)
print(b.name)
print(c.name)
print(d.name)
print(a.name)
print(d.name)