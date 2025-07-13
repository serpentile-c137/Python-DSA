def rotate(matrix):
    n = len(matrix)
 
    for i in range(n):
        for j in range(i, n):
            print(f"Swapping elements at indices with values: ({i}, {j}) and ({j}, {i} => {matrix[i][j]} and {matrix[j][i]})")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print(matrix)

    for row in matrix:
        row.reverse()
        
    print(matrix)
        
matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotate(matrix)