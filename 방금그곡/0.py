def solution(m, musicinfos):
    answer = None
    m = m.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")
    for info in musicinfos:
        start, end, title, scale = info.split(",")
        start = start.split(":")
        end = end.split(":")
        start = int(start[0]) * 60 + int(start[1])
        end = int(end[0]) * 60 + int(end[1])
        minute = end - start
        scale = scale.replace("C#", "1").replace("D#", "2").replace("F#", "3").replace("G#", "4").replace("A#", "5")
        l = len(scale)
        i = 0
        if minute >= l:
            while i < minute:
                if i >= l:
                    scale += scale[i - l]
                i += 1
        else:
            s = ""
            while i < minute:
                s += scale[i]
                i += 1
            scale = s
        if m in scale:
            if not answer or minute > answer[1] or (minute == answer[1] and start < answer[0]):
                answer = (start, minute, title)
    return answer[2] if answer else "(None)"
# 리턴이 None 이면 되는줄 알고 계속 시도했다가 시간만 날렸음...