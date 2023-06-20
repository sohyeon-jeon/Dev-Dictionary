'''
https://school.programmers.co.kr/learn/courses/30/lessons/17683
'''
# 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다
def solution(m, musicinfos):
    answer = []
    # C, C#, D, D#, E, F, F#, G, G#, A, A#, B
    m=m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

    for idx,musicinfo in enumerate(musicinfos):
        info=musicinfo.split(',')

        s_t,s_m=map(int,info[0].split(':'))
        e_t,e_m=map(int,info[1].split(':'))
        play_time=(e_t*60+e_m)-(s_t*60+s_m)

        music=info[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
        play_music=music*(play_time//len(music))+music[:play_time%len(music)]

        if m in play_music:
            answer.append((play_time,idx,info[2]))
            
    if not answer:
        return "(None)"
    else:
        return sorted(answer,key=lambda x:(-x[0],x[1]))[0][2]

#"FOO"
solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"])