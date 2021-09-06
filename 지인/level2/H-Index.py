def solution(citations):
    ans_idx = 0
    citations.sort(reverse=True)
    flag = False
    for i, h in enumerate(citations):
        if i+1 > h:
            ans_idx = i
            flag = True
            break
    if not flag:
        return len(citations)
    return ans_idx