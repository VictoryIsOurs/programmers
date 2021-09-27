def longest(msg, dt):
    l, idx = '', 0
    for i, m in enumerate(msg):
        if dt.get(l+m) is None:
            break
        l += m
        idx = i
    return l, idx

def solution(msg):
    answer = []
    dt = {}
    # 1. 사전 초기화
    for i in range(26):
        dt[chr(ord('A') + i)] = i+1
    
    number = 27
    while len(msg) > 0:
        # 2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w 찾기
        w, idx = longest(msg, dt)
        # 3. w에 해당하는 색인번호 출력하고, 입력에서 w 제거하기
        answer.append(dt[w])
        msg = msg[idx+1:]
        # 4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록하기    
        if len(msg) > 0:
            c = msg[0]
            dt[w+c] = number
            number += 1
            
    return answer