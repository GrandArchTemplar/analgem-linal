# Ввод матрицы 1
m1 = int(input("Введите кол-во строк первой матрицы "))
n1 = int(input("Введите кол-во столбцов первой матрицы "))
matrix1 = []
print("Вводите строки первой матрицы (enter после каждой строки). Элементы в строке разделяйте пробелами")
for i in range(m1):
    a = list(input().split())
    matrix1.append(a)
# Ввод матрицы 2
m2 = int(input("Введите кол-во строк второй матрицы "))
n2 = int(input("Введите кол-во столбцов второй матрицы "))
matrix2 = []
print ("Вводите строки второй матрицы (enter после каждой строки). Элементы в строке разделяйте пробелами")
for i in range(m2):
    a = list(input().split())
    matrix2.append(a)
# Выбираем умножение или сложение
change = int(input("Если вы хотите сложить матрицы, введите 1. Если вы хотите перемножить матрицы, введите 2 "))
if change == 1:
    # сложение
    summa = []
    for i in range(m1):
        summa.append([0]*n1)
    if m1 == m2 and n1 == n2:
        for i in range(m1):
            for j in range(n1):
                summa[i][j] = float(matrix1[i][j]) + float(matrix2[i][j])
        print (summa)
    else:
        print ("Складывать можно только матрицы одинакового размера")
elif change == 2:
    # умножение
    if n1 == m2:
        multiply = []
        for i in range(m1):
            multiply.append([0]*n2)
        # итоговая матрица будет иметь размер m1 на n2
        for i in range(m1):
            for j in range(n2):
                for f in range(n1):
                    multiply[i][j] += float(matrix1[i][f]) * float(matrix2[f][j])
        print (multiply)
    else:
        print ("Перемножать матрицы можно когда кол-во столбцов первой совпадает с кол-вом строк второй")
else:
    print ("Либо 1 либо 2")