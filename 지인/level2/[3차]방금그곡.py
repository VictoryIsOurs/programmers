# 풀긴 했는데 좀 찝찝하다. 너무 C 스타일로 풀었다. 파이토닉한 코드를 향하여 갑시다!
# replace 함수 하나만으로 코드 라인수를 줄일 수 있을 것 같다.
import copy
def solution(m, musicinfos):
    answer = ''
    max_duration = 0
    # m 모양 정제하기 -> m에서 C# -> c 와 같이 변경하기
    ### 이 부분 replace 함수로 대체 가능
    ###############################
    tmp_m = copy.deepcopy(m)
    m = list(m.split('#'))
    m_lst = []
    for i in range(len(m)-1):
        m_lst += list(m[i])
        m_lst[-1] = m_lst[-1].lower()
    if tmp_m[-1] == '#':
        m_lst += m[-1].lower()
    else:
        m_lst += m[-1]
    m = ''.join(m_lst)
    ###############################
    for music in musicinfos:
        # 지속시간 구하기
        music_split = list(music.split(','))
        time1_h, time1_m = int(music_split[0][:2]), int(music_split[0][3:])
        time2_h, time2_m = int(music_split[1][:2]), int(music_split[1][3:])
        if time1_m > time2_m:
            time2_h -= 1
            time2_m += 60
            duration = (time2_m-time1_m) + (time2_h-time1_h) * 60
        else:
            duration = (time2_m-time1_m) + (time2_h-time1_h) * 60
        # 악보 모양 정제하기
        ### 이 부분 replace 함수로 대체 가능
        ###############################
        melody_lst = []
        melody = list(music_split[3].split('#'))
        for i in range(len(melody)-1):
            melody_lst += list(melody[i])
            melody_lst[-1] = melody_lst[-1].lower()
        if music_split[3][-1] == '#':
            melody_lst += melody[-1].lower()
        else:
            melody_lst += melody[-1]
        ###############################
        # 지속시간 길이만큼 악보 길이 만들기
        length = len(melody_lst)
        if duration > length:
            div = duration // length
            mod = duration % length
            melody_lst = melody_lst * div + melody_lst[:mod]
        elif duration < len(melody_lst):
            melody_lst = melody_lst[:duration]
        # 악보에 m이 존재하는지 확인하기        
        if m in ''.join(melody_lst):
            if answer != '':
                if max_duration < duration:
                    answer = music_split[2]
                    max_duration = duration
            else:
                answer = music_split[2]
        if answer == '':
            answer = "(None)"

    return answer


### 남의 풀이
# def shap_to_lower(s):
#     s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
#     return s

# def solution(m,musicinfos):
#     answer=[0,'(None)']   # time_len, title
#     m = shap_to_lower(m)
#     for info in musicinfos:
#         split_info = info.split(',')
#         time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
#         title = split_info[2]
#         part_notes = shap_to_lower(split_info[-1])
#         full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
#         if m in full_notes and time_length>answer[0]:
#             answer=[time_length,title]
#     return answer[-1]