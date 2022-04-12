def make_matrix():
    N = int(input("количество рядов пожалуйста"))
    M = int(input("количество столбцов"))
    matrix = []
    print("извольте написать числа в ряд")
    for i in range(N):
        a = []
        for j in range(M):
            a.append(int(input()))
        matrix.append(a)
    print('Вы ввели:')
    for i in range(N):
        for j in range(M):
            print(matrix[i][j], end = " ")
        print()
    if N != M:
        print("Для не квадратных матриц я искать обратные не умею...")
make_matrix()

def determinant(matrix, det=0):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        D = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        return D