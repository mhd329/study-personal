n = int(input())

call = input().split()

call_list = list(map(int, call))

lowest_num = call_list[0]
for i in call_list:
    if i < lowest_num:
        lowest_num = i

print(lowest_num)