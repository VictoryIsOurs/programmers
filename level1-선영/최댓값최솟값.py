def solution(s):
    list_A = s.split()
    list_B = []
    for i in list_A:
        list_B.append(int(i))

    max_num = list_B[0]
    min_num = list_B[0]
    
    for i in list_B:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
        
    answer = str(min_num) + " " + str(max_num)
    return answer
