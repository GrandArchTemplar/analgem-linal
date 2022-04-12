B = int(input("количество рядов а дай да....."))
C = int(input("атдай количество столбцов"))
matrix1 = []
print("извольте написать числа в ряд")
for i in range(B):
    a = []
    for j in range(C):
         a.append(int(input()))
    matrix1.append(a)
print('Матрица рас:')
for i in range(B):
    for j in range(C):
        print(matrix1[i][j], end=" ")
    print()

D = int(input("нужно больше рядов....!!!!"))
E = int(input("столбцов требуют наши сердцааааа....!!!!"))
matrix2 = []
print("теперь снова числа одно за другим")
for i in range(D):
    a = []
    for j in range(E):
         a.append(int(input()))
    matrix2.append(a)
print('Матрица двас:')
for i in range(D):
    for j in range(E):
        print(matrix2[i][j], end=" ")
    print()


# сложение матриц
if D == B and C == E:
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    print('Вы восхитительны, ваш результат:')
    for r in result:
        print(r)
else:
    print("матрицы слишком разные чтобы сочетаться вечным сложением и союзом любви.....")


# умножение матриц
if C == D:
    comp = [[0 for _ in range(B)] for _ in range(E)]
    for i in range(E):
        for j in range(B):
            comp[i][j] = sum(matrix1[i][k] * matrix2[k][j] for k in range(C))
    print('А если умножить, получится это:')
    for c in comp:
        print(c)
else:
    print('Я вам запрещаю такие матрицы умножать!')