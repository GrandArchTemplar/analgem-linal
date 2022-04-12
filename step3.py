def make_matrix():
    B = 3
    C = 3
    matrix = []
    print("извольте написать числа в ряд")
    for i in range(B):
        a = []
        for j in range(C):
            a.append(int(input()))
        matrix.append(a)
    print('Вы создали:')
    for i in range(B):
        for j in range(C):
            print(matrix[i][j], end = " ")
        print()
    return matrix

def polinom(matrix):
    a = str(-1) + 'xxx'
    b = '+' + str(matrix[2][2] + matrix[0][0] + matrix[1][1]) + 'xx'
    c = '+' + str(-matrix[0][0] * matrix[2][2] - matrix[1][1] * matrix[2][2] - matrix[1][1] * matrix[0][0] +
                  matrix[0][2] * matrix[2][0] + matrix[1][2] * matrix[2][1] + matrix[1][0] * matrix[0][1]) + 'x'
    d = '+' + str(matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] +
                  matrix[0][2] * matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[0][2] * matrix[2][0] -
                  matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[2][2] * matrix[0][1] * matrix[1][0])
    result = a + b + c + d
    print(result)
polinom(make_matrix())