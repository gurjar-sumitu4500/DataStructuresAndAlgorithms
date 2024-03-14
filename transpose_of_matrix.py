def transpose(matrix):
    newMatrix = []
    max_length = max(len(i) for i in matrix)
    for a in matrix:
        a.extend([0] * (max_length - len(a)))
    for i in range(max_length):
        arr = []
        for j in range(len(matrix)):
            arr.append(matrix[j][i])
        newMatrix.append(arr)
    return newMatrix
