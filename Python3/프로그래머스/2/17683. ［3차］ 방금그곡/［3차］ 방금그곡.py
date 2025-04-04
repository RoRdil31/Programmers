from datetime import datetime as dt
def solution(m, musicinfos):
    ans_time, answer = -1, ''
    m = m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    
    for music in musicinfos:
        t1, t2, title, content = music.split(',')
        content = content.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
        diff = int((dt.strptime(t2,'%H:%M')-dt.strptime(t1,'%H:%M')).total_seconds()//60)
        content *= (diff//len(content)) + 1
        content = content[:diff]
        if content.find(m) != -1 and diff > ans_time : answer = title; ans_time = diff
        
    
    return answer if answer else '(None)'





















# from datetime import datetime as dt
# def solution(m, musicinfos): # 라디오 재생 긴 것, 먼저 입력된 음악.
#     candidates = []
#     def convert_music(music):
#         return music.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    
#     m = convert_music(m)
    
#     for info in musicinfos:
#         t1, t2, title, music = info.split(',')
#         play_time = int((dt.strptime(t2,'%H:%M')-dt.strptime(t1,'%H:%M')).total_seconds()//60)
#         music = convert_music(music)
        
#         full_music = (music*((play_time//len(music))+1))[:play_time]
        
#         if m in full_music: candidates.append((play_time, title))
            
#     return sorted(candidates, key = lambda x : (-x[0]))[0][1] if candidates else "(None)"