def solution(m, n, board):
    board = [list(x) for x in board]
    answer = 0

    while True:
        flag = False

        check = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i+1 < m and j+1 < n and board[i][j] != '#' and board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    check[i][j], check[i+1][j], check[i][j+1], check[i+1][j+1] = 1, 1, 1, 1
                    flag = True

        if not flag: break

        for j in range(n):
            tmp = []
            for i in range(m):
                if not check[i][j]:
                    tmp.append(board[i][j])
            answer += (m-len(tmp))
            tmp = ['#']*(m - len(tmp)) + tmp
            for i in range(m):
                board[i][j] = tmp[i]

    return answer