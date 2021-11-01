def quad_tree(arr, n, x, y, table):    
    if n == 1:
        table[arr[x][y]] += 1
        return
    
    flag = True
    for i in range(x, x+n):
        if not flag: break
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:
                flag = False
                break    
    if flag: 
        table[arr[x][y]] += 1
        return  
    
    quad_tree(arr, n//2, x, y, table)
    quad_tree(arr, n//2, x, y+n//2, table)
    quad_tree(arr, n//2, x+n//2, y, table)
    quad_tree(arr, n//2, x+n//2, y+n//2, table)
    
def solution(arr):
    n = len(arr)
    table = [0, 0]
    quad_tree(arr, n, 0, 0, table)
    return table