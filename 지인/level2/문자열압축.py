def solution(s):
    if len(s) == 1:
        return 1

    answer_list = []
    for i in range(len(s)//2):
        split_num, split_list = i+1, []
        idx = 0
        while idx < len(s):
            split_list.append(s[idx:idx + split_num])
            idx += split_num

        tmp, cnt, sum = split_list[0], 1, 0
        for i in range(1, len(split_list)):
            if tmp == split_list[i]:
                cnt += 1
            else:
                if cnt > 1:
                    sum += len(str(cnt)) + len(tmp)
                else:
                    sum += len(tmp)
                cnt = 1
                tmp = split_list[i]
        if cnt > 1:
            sum += len(str(cnt)) + len(tmp)
        else:
            sum += len(tmp)
        answer_list.append(sum)
    return min(answer_list)