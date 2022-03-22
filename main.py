row = int(input("Введите количество строк первой матрицы: "))
col = int(input("Введите количество столбцов первой матрицы: "))
print("Введите элементы по одному(движемся слева направо, сверху вниз): ")
final_matrix_1 = []
for i in range(row):
    sub_matrix_1 = []
    for j in range(col):
        sub_matrix_1.append(int(input()))
    final_matrix_1.append(sub_matrix_1)
print(final_matrix_1)

row2 = int(input("Введите количество строк второй матрицы: "))
col2 = int(input("Введите количество столбцов второй матрицы: "))
print("Введите элементы: ")
final_matrix_2 = []
for i in range(row2):
    sub_matrix_2 = []
    for j in range(col2):
        sub_matrix_2.append(int(input()))
    final_matrix_2.append(sub_matrix_2)
print(final_matrix_2)

if row != row2 or col != col2:
    print("ПОДУМОЙ! Нельзя складывать матрицы разных размерностей!")

if row == row2 and col == col2:
    mother_matrix = []
    m = 0
    n = 0
    for i in range(row2):
        sub_matrix = []
        for j in range(col2):
            sub_matrix.append(final_matrix_1[m][n] + final_matrix_2[m][n])
            n += 1
        mother_matrix.append(sub_matrix)
        m += 1
        n = 0
    print("Внимание, суммируем... иии... ответ!: ", mother_matrix)

if col != row2:
    print("К сожалению, такие матрицы перемножать нельзя, нужно чтобы количество столбцов первой матрицы равнялось количеству строк второй")

if col == row2:
    n = 0
    new = 0
    father_matrix = []
    for i in range(row):
        sub_matrix = []
        while n < col2:
            for j in range(col):
                new = new + final_matrix_1[i][j] * final_matrix_2[j][n]
            sub_matrix.append(new)
            new = 0
            n += 1
        new = 0
        n = 0
        father_matrix.append(sub_matrix)
    print("Теперь посчитаем произведение матриц(!): ", father_matrix)