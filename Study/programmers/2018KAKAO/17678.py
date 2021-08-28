#[1차] 셔틀버스

from collections import deque
def solution(n, t, m, timetable):
    timetable = sorted(timetable,reverse=True)
    # 셔틀버스 타임테이블 만들기
    bus_timetable = {}
    s_time = '09:00'
    bus_timetable[s_time] = deque(maxlen=m)
    for i in range(1,n):
        s_time_m = int(s_time[3:])
        s_time_h = int(s_time[0:2])
        s_time_m += t
        if s_time_m>59:
            s_time_m -= 60
            s_time_h += 1
        s_time = str(s_time_h).zfill(2)+':'+str(s_time_m).zfill(2)
        bus_timetable[s_time] = deque(maxlen=m)

    #탑승 시키기
    for key in bus_timetable:    
        for time in timetable:
            if time <= key:
                bus_timetable[key].append(time)
                continue
                
    for key in reversed(bus_timetable):
        if len(bus_timetable[key]) == m:
            if len(set(bus_timetable[key])) == 1:
                t = bus_timetable[key][0]
                hour = int(t[0:2])
                min = int(t[3:])-1
                if min < 0:
                    answer = str(hour-1).zfill(2)+':59'
                else:
                    answer = str(hour).zfill(2)+':'+str(min).zfill(2)

            else:
                answer = sorted(bus_timetable[key])[0]
        else:
            answer = key
        break
    
    print()
    print(timetable)
    print(bus_timetable)
    print(answer)
    return answer

solution(1,1,5,	["08:00", "08:01", "08:02", "08:03"])
solution(2,10,2,["09:10", "09:09", "08:00"])
solution(2,1,2,["09:00", "09:00", "09:00", "09:00"])
solution(1,1,5,	["00:01", "00:01", "00:01", "00:01", "00:01"])
solution(1,1,1,["23:59"])
solution(10,60,45,["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])