from datetime import datetime
def solution(book_time):
    init_time = datetime.strptime('00:00', '%H:%M')
    dic = {1:init_time}
    book_time = sorted(book_time, key = lambda x : x[:5])

    room_num = 1
    for time in book_time:
        t1 = datetime.strptime(time[0], '%H:%M')
        t2 = datetime.strptime(time[1], '%H:%M')
        new_room = True
        for idx, value in dic.items():
            if (t1 - value).total_seconds()/60 >= 10:
                dic[idx] = t2
                new_room = False
                break
        if new_room :
            room_num += 1
            dic[room_num] = t2
    
    return len(dic)