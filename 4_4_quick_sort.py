def multiple_matrix(arr):
    b = arr
    matrix = []
    for i in arr:
        c = []
        for j in b:
            c.append(i * j)
        matrix.append(c)
    return matrix
print(multiple_matrix([1, 2, 3]))

def mul_mat(arr):
    b = {}
    matrix = []
    for i in arr:
        b[i] = [x * i for x in arr]
        matrix.append(b[i])
    return matrix

print(mul_mat([1, 2, 3]))