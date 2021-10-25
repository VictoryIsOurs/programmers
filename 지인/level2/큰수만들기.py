def solution(number, k):
    stack, idx = [], -1
    for i, n in enumerate(number):
        if not stack: stack.append(n)
        else:
            if stack[-1] >= n: stack.append(n)
            else:
                while stack and k > 0 and stack[-1] < n:
                    stack.pop()
                    k -= 1
                stack.append(n)
        if k == 0:
            idx = i
            break
    if k: stack.pop() # number='1', k=1 일 경우
    return ''.join(stack) + number[i+1:]