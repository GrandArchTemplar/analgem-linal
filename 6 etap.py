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
    print('Пожалуйста, введите квадратную матрицу. Мы сможем проверить на унитарность только квадратную.')

def minor_of_dopolneniya(final_matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (final_matrix[:i] + final_matrix[i + 1:])]

def determinant(final_matrix):
    s = 0
    if len(final_matrix) == 1:
        return final_matrix[0][0]
    if len(final_matrix) == 2:
        return final_matrix[0][0] * final_matrix[1][1] - final_matrix[0][1] * final_matrix[1][0]
    else:
        for j in range(len(final_matrix)):
            s += (-1) ** (j + 1) * final_matrix[0][j] * determinant(minor_of_dopolneniya(final_matrix, 0, j))
        return -s

print("Определитель матрицы равен ", determinant(final_matrix))
det = determinant(final_matrix)

transposed_istina = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(final_matrix[j][i])
    transposed_istina.append(sub_matrix)

if det == 0:
    print("неунитарная")
if det != 0:
    if len(final_matrix) != 2:
        matrix_of_dopolneniy = []
        for i in range(row):
            sub_matrix = []
            for j in range(col):
                sub_matrix.append(((-1) ** (i + j)) * determinant(minor_of_dopolneniya(final_matrix, i, j)))
            matrix_of_dopolneniy.append(sub_matrix)
    else:
        matrix_of_dopolneniy = [[final_matrix[1][1], final_matrix[0][1]],[final_matrix[1][0], final_matrix[0][0]]]
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
    if transposed_istina == inverse_matrix:
        print('унитарная')
    else:
        print('неунитарная')
if final_matrix == transposed_istina:
    print('самосопряженная')
else:
    print('несамосопряженная')
