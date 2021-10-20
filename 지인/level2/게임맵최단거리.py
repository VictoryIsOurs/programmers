from collections import deque

def solution(maps):
    answer = 0
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    row, col = len(maps), len(maps[0])
    dist = [[-1]*col for _ in range(row)]
    queue = deque()
    queue.append([0, 0])
    dist[0][0] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<row and 0<=ny<col and maps[nx][ny]:
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append([nx, ny])
    return dist[-1][-1]