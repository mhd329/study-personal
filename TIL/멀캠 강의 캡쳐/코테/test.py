def solution(today, terms, privacies):
    answer = []
    terms_info = {}

    for i in terms:
        temp = i.split(' ')
        terms_info[temp[0]] = int(temp[1])

    today = today.split('.')

    today_year = int(today[0])
    today_month = int(today[1])
    today_day = int(today[2])

    for privacies_info in privacies:
        privacies_date = privacies_info.split(' ')[0]
        privacies_period = privacies_info.split(' ')[1]
        
        temp = privacies_date.split('.')

        privacies_year = int(temp[0])
        privacies_month = int(temp[1])
        privacies_day = int(temp[2])

        for _ in range(terms_info[privacies_period]):
            privacies_month += 1
            if privacies_month > 12:
                privacies_month = 1
                privacies_year += 1

        privacies_day -= 1
        if privacies_day < 1:
            privacies_day = 28
            privacies_month -= 1
            if privacies_month <= 0:
                privacies_year -= 1
                privacies_month = 12

        if today_year > privacies_year:
            answer.append(privacies.index(privacies_info) + 1)
        elif today_month > privacies_month:
            answer.append(privacies.index(privacies_info) + 1)
        elif today_day > privacies_day:
            answer.append(privacies.index(privacies_info) + 1)
        print(privacies_year,privacies_month,privacies_day)
    print(answer)
    return answer

solution("2020.01.01", ["Z 100", "D 1", "A 60"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z", "2018.12.01 A"])