def solution(files):
    answer = []
    file_list = []
    dt = {}

    for i, file in enumerate(files):
        head, number = '', ''
        flag = False
        for f in file:
            if not f.isdigit() and not flag:
                head += f
            elif f.isdigit():
                flag = True
                number += f
            else:
                break
        file_list.append((head.lower(), int(number), i))
        dt[(head.lower(), int(number), i)] = file
    file_list.sort(key = lambda x : (x[0], x[1], x[2]))
    for f in file_list:
        answer.append(dt[f])
    return answer