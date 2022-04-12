row = int(input("Введите количество строк матрицы: "))
col = int(input("Введите количество столбцов матрицы: "))
print("Введите элементы по одному(движемся слева направо, сверху вниз): ")
final_matrix = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(int(input()))
    final_matrix.append(sub_matrix)
print('Ваша матрица:) Убедитесь, пожалуйста, что все правильно ввели: ', final_matrix)

if row != col:
    print('Обратную матрицу можно найти только для квадратной матрицы! Введите квадратную!')

def determinant(final_matrix, det=0):
    indx = list(range(len(final_matrix)))
    if len(final_matrix) == 2 and len(final_matrix[0]) == 2:
        a = final_matrix[0][0] * final_matrix[1][1] - final_matrix[0][1] * final_matrix[1][0]
        return a
    for i in indx:
        minor = final_matrix[1:]
        RowMinor = row - 1
        for j in range(RowMinor):
            minor[j] = minor[j][0:i] + minor[j][i + 1:]
        sign = (-1) ** (i % 2)
        MiniDet = determinant(minor)
        det += sign * final_matrix[0][i] * MiniDet
    return det

print("Определитель матрицы равен ", determinant(final_matrix))
det = determinant(final_matrix)

def minor_of_dopolneniya(final_matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (final_matrix[:i] + final_matrix[i + 1:])]

if det == 0:
    print("Это вырожденная матрица! К сожалению, у неё нет обратной")
if det != 0:
    matrix_of_dopolneniy = []
    for i in range(row):
        sub_matrix = []
        for j in range(col):
            sub_matrix.append(((-1) ** (i + j)) * determinant(minor_of_dopolneniya(final_matrix, i, j)))
        matrix_of_dopolneniy.append(sub_matrix)
    transposed = []
    for i in range(row):
        sub_matrix = []
        for j in range(col):
            sub_matrix.append(matrix_of_dopolneniy[j][i])
        transposed.append(sub_matrix)
    inverse_matrix = []
    for i in range(row):
        sub_matrix = []
        for j in range(col):
            sub_matrix.append(float(transposed[i][j]) / det)
        inverse_matrix.append(sub_matrix)
    print('Ответ! ', inverse_matrix)