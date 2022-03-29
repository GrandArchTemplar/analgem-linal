row = int(input("Введите количество строк в матрице:"))
column = int(input("Введите количество столбцов в матрице:"))
A = []

print("Введите данные по строкам слева направо:")
for i in range(row):
    a = []
    for j in range(column):
        a.append(float(input()))
    A.append(a)
print(" ")
print("матрица:")
for i in range(row):
    for j in range(column):
        print(A[i][j], end=" ")
    print()
def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def minor(matrix, i, j):
    tmp = [row for k, row in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp

def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det(matrix)
    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

if row == column and row!=1:
    print("определитель:",determinant(A))
    if determinant(A)!=0:
        M = []
        for i in range(row):
            m = []
            for j in range(column):
                m.append(0)
            M.append(m)
        for i in range(row):
            for j in range(column):
                M[i][j] = (-1) ** (i + j) * determinant(minor(A, i, j))

        T = []
        for i in range(row):
            t = []
            for j in range(column):
                t.append(0)
            T.append(t)
        for i in range(row):
            for j in range(column):
                T[j][i] = M[i][j]
        print("Обратная матрица:")
        B = []
        for i in range(row):
            b = []
            for j in range(column):
                b.append(0)
            B.append(b)
        kek = 1 / determinant(A)
        if row != 2:
            for i in range(row):
                for j in range(column):
                    B[i][j] = T[i][j] * kek
                    print(B[i][j], end=" ")
                print()
        else:
            M[0][0] = A[1][1]
            M[0][1] = A[1][0] * -1
            M[1][0] = A[0][1] * -1
            M[1][1] = A[0][0]
            for i in range(row):
                for j in range(column):
                    T[j][i] = M[i][j]
            for i in range(row):
                for j in range(column):
                    B[i][j] = T[i][j] * kek
                    print(B[i][j], end=" ")
                print()


elif row == column and row==1:
    print("определитель:", A[0][0])
    print("обратный элемент:",1/A[0][0])
else:
    print("невозможно посчитать определитель") 