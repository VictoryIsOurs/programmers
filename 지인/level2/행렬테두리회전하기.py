import copy
def solution(rows, columns, queries):
    answer = []
    matrix = [[i + (j) * columns for i in range(1, columns + 1)] for j in range(rows)]
    tmp_matrix = copy.deepcopy(matrix)

    for query in queries:
        min_lst = []
        x1, y1, x2, y2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        x, y = x1, y1
        # right
        for i in range(1, y2 - y1 + 1):
            tmp_matrix[x][y + i] = matrix[x][y + i - 1]
            min_lst.append(matrix[x][y + i - 1])
        # down
        y += (y2 - y1)
        for i in range(1, x2 - x1 + 1):
            tmp_matrix[x + i][y] = matrix[x + i - 1][y]
            min_lst.append(matrix[x + i - 1][y])
        # left
        x, y = x2, y2
        for i in range(1, y2 - y1 + 1):
            tmp_matrix[x][y - i] = matrix[x][y - i + 1]
            min_lst.append(matrix[x][y - i + 1])
        # up
        y -= (y2 - y1)
        for i in range(1, x2 - x1 + 1):
            tmp_matrix[x - i][y] = matrix[x - i + 1][y]
            min_lst.append(matrix[x - i + 1][y])
        answer.append(min(min_lst))

        for i in range(rows):
            for j in range(columns):
                if tmp_matrix[i][j] != matrix[i][j]:
                    matrix[i][j] = tmp_matrix[i][j]
    return answer