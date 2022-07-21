import sys
sys.stdin = open("input.txt", 'r')

t = int(input())

for test_case in range(1, t + 1):
    date = input() # 22220228
    
    month = int(date[4:6])
    day = int(date[6:8])
    
    if month <= 12 and month >= 1:
        if day > 0:
            if day <= 31:
                if month == 4 or month == 6 or month == 9 or month == 11:
                    print(f"#{test_case} {date[0:4] + '/' + date[4:6]  + '/' + date[6:8]}")
                elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                    print(f"#{test_case} {date[0:4] + '/' + date[4:6]  + '/' + date[6:8]}")
                elif month == 2 and day <= 28:
                    print(f"#{test_case} {date[0:4] + '/' + date[4:6]  + '/' + date[6:8]}")
                else:
                    print(f"#{test_case} {-1}")
    else:
        print(f"#{test_case} {-1}")
        
# 집중력이 너무 떨어져서 급하게 마무리했다.