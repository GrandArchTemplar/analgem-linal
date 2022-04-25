i1 = int(input("Количество строчек матрицы 1: "))
j1 = int(input("Количество столбцов матрицы 1: "))
A=[]
print("Введите элементы матрицы слева направо по одному, по строчкам: ")
for i in range(i1):
    a = []
    for j in range(j1):
        a.append(float(input()))
    A.append(a)
print(" ")
print("матрица:")
for i in range(i1):
    for j in range(j1):
        print(A[i][j], end=" ")
    print()
def det(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def minor(matrix, i, j):
    tmp = [i1 for k, i1 in enumerate(matrix) if k != i]
    tmp = [col for k, col in enumerate(zip(*tmp)) if k != j]
    return tmp

def determinant(matrix):
    size = len(matrix)
    if size == 2:
        return det(matrix)
    return sum((-1) ** j * matrix[0][j] * determinant(minor(matrix, 0, j))
               for j in range(size))

if i1 == j1 and i1 != 1:
    print("определитель:",determinant(A))
    if determinant(A)!=0:
        M = []
        for i in range(i1):
            m = []
            for j in range(j1):
                m.append(0)
            M.append(m)
        for i in range(i1):
            for j in range(j1):
                M[i][j] = (-1) ** (i + j) * determinant(minor(A, i, j))

        T = []
        for i in range(i1):
            t = []
            for j in range(j1):
                t.append(0)
            T.append(t)
        for i in range(i1):
            for j in range(j1):
                T[j][i] = M[i][j]
        print("Обратная матрица:")
        B = []
        for i in range(i1):
            b = []
            for j in range(j1):
                b.append(0)
            B.append(b)
        kek = 1 / determinant(A)
        if i1 != 2:
            for i in range(i1):
                for j in range(j1):
                    B[i][j] = T[i][j] * kek
                    print(B[i][j], end=" ")
                print()
        else:
            M[0][0] = A[1][1]
            M[0][1] = A[1][0] * -1
            M[1][0] = A[0][1] * -1
            M[1][1] = A[0][0]
            for i in range(i1):
                for j in range(j1):
                    T[j][i] = M[i][j]
            for i in range(i1):
                for j in range(j1):
                    B[i][j] = T[i][j] * kek
                    print(B[i][j], end=" ")
                print()

elif i1 == j1 and i1 == 1:
    print("Определитель:", A[0][0])
    print("Обратный элемент:",1/A[0][0])
else:
    print("Невозможно посчитать определитель")