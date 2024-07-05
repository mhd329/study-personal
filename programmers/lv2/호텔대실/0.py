# 엄청 무식하게 풀었다.
def solution(book_time):
    answer = 0
    l = len(book_time)
    rooms = []
    # book_time.sort(key=lambda x: [*map(int, [i.replace(":", "") for i in x])][0])
    # 이것은 정렬만 되고 실제 int로 변하지는 않았음
    book_time = [[int(j.replace(":", ""))for j in i] for i in book_time]
    book_time.sort(key=lambda x: x[0])
    # 1번 손님을 1번방에
    # 2번 손님을 1번방에 배정 가능한지, 가능하지 않다면 2번방에
    # 3번 손님을 1번방, 2번방에 배정 가능한지, 가능하지 않다면 3번방에
    
    # 4번 손님 i => i == 4
    # while, i += 1, i는 손님 번호 and 방 번호
    # for문, range(len(book_time)), i, i가 1일때 그냥 추가
    # i가 2일때는 1번방 일정 탐색후 1번방의 뒤에 붙일지 2번 새로 추가할지
    # i가 3일때는 1번 2번 일정 탐색후 위의 작업 반복

    # 같은방 쓰는경우
    # 기존에 있던 손님의 퇴실시간보다 새로운 손님의 입실시간이 10분이상 늦거나
    # 기존에 있던 손님의 입실시간보다 새로운 손님의 퇴실시간이 10분이상 빨라야 한다.

    book_list = []
    for i in range(l):
        # i => 0 ~ 4 까지
        # 0번 손님에 대해,
        if not rooms:
            # 0번 방에 0번 손님의 입실 퇴실 시간 추가
            rooms.append([book_time[i][0], book_time[i][1]])
            book_list.append(i)
        else:
            # 1번 손님에 대해,
            # 0번 방 부터 끝까지 돌면서 일정을 확인해야한다.
            for j in range(len(rooms)):
                # j는 방번호
                # rooms[j]
                # rooms[j][0] 기존 입실
                # rooms[j][1] 기존 퇴실
                new_room_out = str(book_time[i][1] + 9)
                old_room_out = str(rooms[j][-1] + 9)
                if new_room_out[-2] == '6':
                    new_room_out = list(new_room_out)
                    new_room_out[-2] = '0'
                    try:
                        new_room_out[:-2] = str(int(''.join(new_room_out[:-2])) + 1)
                        new_room_out = ''.join(new_room_out)
                    except:
                        new_room_out[:-1] = str(int(''.join(new_room_out[:-1])) + 1)
                        new_room_out = ''.join(new_room_out)
                new_room_out = int(new_room_out)
                if old_room_out[-2] == '6':
                    old_room_out = list(old_room_out)
                    old_room_out[-2] = '0'
                    try:
                        old_room_out[:-2] = str(int(''.join(old_room_out[:-2])) + 1)
                        old_room_out = ''.join(old_room_out)
                    except:
                        old_room_out[:-1] = str(int(''.join(old_room_out[:-1])) + 1)
                        old_room_out = ''.join(old_room_out)
                old_room_out = int(old_room_out)
                if rooms[j][0] > new_room_out or old_room_out < book_time[i][0]:
                    if not i in book_list:
                        rooms[j].extend([book_time[i][0], book_time[i][1]])
                        book_list.append(i)
                        rooms[j].sort()
            else:
                if not i in book_list:
                    rooms.append([book_time[i][0], book_time[i][1]])
                    book_list.append(i)
    answer = len(rooms)
    return answer

# 나처럼 하드코딩 안하고 그냥 푼 코드

def solution(book_time):
    time_table = [0 for _ in range(60 * 24)]
    for start, end in book_time:
        start_minutes = 60 * int(start[:2]) + int(start[3:])
        end_minutes = 60 * int(end[:2]) + int(end[3:]) + 10

        if end_minutes > 60 * 24 - 1:
            end_minutes = 60 * 24 - 1

        for i in range(start_minutes, end_minutes):
            time_table[i] += 1
    return max(time_table)