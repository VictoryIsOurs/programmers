def dfs(n, i, computers, visited):
    visited[i] = 1
    for j in range(n):
        if computers[i][j] and not visited[j]:
            dfs(n, j, computers, visited)

def solution(n, computers):
    answer = 0
    visited = [0]*n
    for i in range(n):
        if not visited[i]:
            dfs(n, i, computers, visited)
            answer += 1
    return answer