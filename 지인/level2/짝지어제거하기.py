def solution(ss):
    stack = []
    for s in ss:
        if not stack:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            else:
                stack.append(s)
    if not stack: return 1
    else: return 0