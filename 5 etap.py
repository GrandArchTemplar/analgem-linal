import math

row = 2
col = 2
print("Введите элементы матрицы 2 х 2 по одному(движемся слева направо, сверху вниз): ")
final_matrix = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(float(input()))
    final_matrix.append(sub_matrix)
print('Ваша матрица:) Убедитесь, пожалуйста, что все правильно ввели: ', final_matrix)

d = (final_matrix[0][0] + final_matrix[1][1])**2 - 4*(final_matrix[0][0]*final_matrix[1][1] - final_matrix[1][0]*final_matrix[0][1])
l1 = round((final_matrix[0][0] + final_matrix[1][1] + math.sqrt(d))/2, 4)
l2 = round((final_matrix[0][0] + final_matrix[1][1] - math.sqrt(d))/2, 4)

print('Внимание! Представляем вам собственные значения!')
print("Значение раз: ", l1)
print("Значение два: ", l2)

if final_matrix[0][0] - l1 != 0 and final_matrix[0][1] != 0:
    x1 = 1
    y1 = round(-(final_matrix[0][0] - l1)/final_matrix[0][1], 4)
elif final_matrix[1][1] - l1 != 0:
    x1 = 1
    y1 = round(-final_matrix[1][0]/(final_matrix[1][1] - l1), 4)
else:
    x1 = 0
    y1 = 1

if final_matrix[0][0] - l2 != 0 and final_matrix[0][1] != 0:
    x2 = 1
    y2 = round(-(final_matrix[0][0] - l2)/final_matrix[0][1], 4)
elif final_matrix[1][1] - l2 != 0:
    x2 = 1
    y2 = round(-final_matrix[1][0]/(final_matrix[1][1] - l2), 4)
else:
    x2 = 0
    y2 = 1

t = [[x1, x2], [y1, y2]]


def determinant(final_matrix, det=0):
    indx = list(range(len(final_matrix)))
    if len(final_matrix) == 2 and len(final_matrix[0]) == 2:
        a = final_matrix[0][0] * final_matrix[1][1] - final_matrix[0][1] * final_matrix[1][0]
        return a
    for i in indx:
        minor = final_matrix[1:]
        RowMinor = 2 - 1
        for j in range(RowMinor):
            minor[j] = minor[j][0:i] + minor[j][i + 1:]
        sign = (-1) ** (i % 2)
        MiniDet = determinant(minor)
        det += sign * final_matrix[0][i] * MiniDet
    return det

det = determinant(t)

def minor_of_dopolneniya(final_matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (final_matrix[:i] + final_matrix[i + 1:])]

if det == 0:
    print("Это вырожденная матрица! К сожалению, у неё нет обратной и, соответственно, у неё нет проекторов")

if det != 0:
    matrix_of_dopolneniy = [[t[1][1], t[0][1]], [t[1][0], t[0][0]]]
    transposed = []
    for i in range(row):
        sub_matrix = []
        for j in range(col):
            sub_matrix.append(matrix_of_dopolneniy[j][i])
        transposed.append(sub_matrix)
    inverse_t = []
    for i in range(row):
        sub_matrix = []
        for j in range(col):
            sub_matrix.append(float(transposed[i][j]) / det)
        inverse_t.append(sub_matrix)

if det != 0:
    for number in range(2):
        matrix1 = [[t[0][number]], [t[1][number]]]
        matrix2 = [[inverse_t[number][0], inverse_t[number][1]]]
        proector = [[matrix1[0][0] * matrix2[0][0], matrix1[0][0] * matrix2[0][1]], [matrix1[1][0] * matrix2[0][0], matrix1[1][0] * matrix2[0][1]]]
        if number == 0:
            print("Проектор для значения l1=", l1, ": ", proector)
        else:
            print("Проектор для значения l2=", l2, ": ", proector)
