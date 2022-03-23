strochki = int(input("Количество строчек первой матрицы: "))
kolonki = int(input("Количество столбцов первой матрицы: "))
matrix=[]
print("Введите элементы матрицы слева направо по одному, по строчкам: ")
for i in range(strochki):
    a = []
    for j in range(kolonki):
        a.append(float(input()))
    matrix.append(a)
strochki1 = int(input("Количество строчек второй матрицы: "))
kolonki1 = int(input("Количество столбцов второй матрицы: "))
matrix1=[]
print("Введите элементы матрицы слева направо по одному, по строчкам: ")
for i in range(strochki1):
    b = []
    for j in range(kolonki1):
        b.append(float(input()))
    matrix1.append(b)
for i in range(strochki):
   for j in range(kolonki):
      print(matrix[i][j], end = " ")
   print()
for i in range(strochki1):
   for j in range(kolonki1):
      print(matrix1[i][j], end = " ")
   print()
matrix666=[]
tip = int(input("Введите тип операции: 228 - умножение, 666 - сложение: "))
if tip==666:
    if strochki != strochki1 and kolonki != kolonki1:
        print("error - разные размерности матриц")
    else:
        for i in range(strochki):
            c = []
            for j in range(kolonki):
                c.append(0)
            matrix666.append(c)
        for i in range(strochki):
            for k in range(kolonki):
                matrix666[i][k] = matrix[i][k] + matrix1[i][k]
        for i in range(strochki):
            for j in range(kolonki):
                print(matrix666[i][j], end=" ")
            print()
if tip==228:
    if kolonki!=strochki1:
        print("error - умножение невозможно")
    else:
        for z in range(strochki):
            t=[]
            s=0
            for j in range(kolonki1):
                for i in range(kolonki):
                   s=s+matrix[z][i]*matrix1[i][j]
                t.append(s)
                s=0
            matrix666.append(t)
            t=[]
        for i in range(strochki):
            for j in range(kolonki1):
                print(matrix666[i][j], end=" ")
            print()


