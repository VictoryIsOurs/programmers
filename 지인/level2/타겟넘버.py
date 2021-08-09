answer = 0

def dfs(idx, numbers, target, value):
    global answer
    n = len(numbers)
    if idx == n and target == value:
        answer += 1
        return
    if idx == n:
        return

    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer