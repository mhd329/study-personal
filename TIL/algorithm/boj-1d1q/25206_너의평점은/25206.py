import sys
sys.stdin = open("25206.txt", 'r')
score = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0.0
}
res = []
total_point = 0
for _ in range(20):
    subject, point, grade = sys.stdin.readline().split()
    point = float(point)
    if grade != 'P':
        res.append(point * score[grade])
        total_point += point
print(sum(res)/total_point)