import datetime
def solution(today, terms, privacies):
    answer = []
    today = today.replace(".", "-")
    today = datetime.date.fromisoformat(today)
    j = 1
    for p in privacies:
        for t in terms:
            if p.split()[1] == t.split()[0]:
                i = 0
                ymd = p.split()[0].split(".")
                y = int(ymd[0])
                m = int(ymd[1])
                d = int(ymd[2])
                while i < int(t.split()[1]):
                    m += 1
                    if m > 12:
                        m = 1
                        y += 1
                    i += 1
                d -= 1
                if d == 0:
                    m -= 1
                    d = 28
                    if m == 0:
                        m = 12
                        y -= 1
                ymd = datetime.date(y, m, d)
                if today > ymd:
                    answer.append(j)
        j += 1
    return answer