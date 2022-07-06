class ListPriorityQueue:
    def __init__(self):
        self.my_list = []

    def put(self, element):
        self.my_list.append(element)
        self.my_list.sort(key=lambda x: x) # 왜 예문을 만든 사람은 x : x[0] 이라고 했을까? 그렇게 했더니 오류가 났는데 어떤 착오가 있는것일까?
        
        # 람다 x 가 for[i] 형태인것같다. 그래서 for[i] 는 int 니까 int[0] 은 당연히 안되니 오류가 나는것일까 ?

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)
    
lst1 = ListPriorityQueue()

lst1.put(5)
lst1.put(2)
lst1.put(7)
lst1.put(3)
lst1.put(4)
lst1.put(1)

print(lst1.my_list)
print(lst1.qsize())