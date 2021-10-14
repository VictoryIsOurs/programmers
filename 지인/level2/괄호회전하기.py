def check(s):
    stack = []
    dt = {')':'(', '}':'{', ']':'['}
    for a in s:
        if a == '(' or a == '{' or a == '[':
            stack.append(a)
        elif a == ')' or a == '}' or a == ']':
            if not stack:
                return False
            elif stack[-1] != dt[a]:
                return False
            elif stack[-1] == dt[a]:
                stack.pop()
    if not stack:
        return True
    else:
        return False
def solution(s):
    answer = 0
    s_list = list(s)
    for i in range(len(s)):
        if check(''.join(s_list)):
            answer += 1
        s_list.append(s_list.pop(0))
    return answer