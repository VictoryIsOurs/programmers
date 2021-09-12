def split_str(my_str):
    str_list = []
    for i in range(0, len(my_str)-1):
        s = my_str[i:i+2]
        if s[0].isalpha() and s[1].isalpha():
            str_list.append(s)
    return str_list

def solution(str1, str2):
    str1, str2 = str1.upper(), str2.upper()
    str1_list, str2_list = split_str(str1), split_str(str2)
    if len(str1_list) == 0 and len(str2_list) == 0:
        return 65536

    inter = 0
    bool_list = [False]*len(str2_list)
    for s in str1_list:
        for i in range(len(str2_list)):
            if s == str2_list[i] and not bool_list[i]:
                bool_list[i] = True
                inter += 1
                break
    union = len(str1_list) + len(str2_list) - inter
    return int(inter/union*65536)