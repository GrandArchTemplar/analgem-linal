
# функция возвращающая IJ минор
def minor(a, I, J):
    res = []
    for i in range(len(a)):
        if i == I:
            continue
        else:
            if len(a[i])==2:
                if J == 0:
                    res.append(a[i][1])
                elif J == 1:
                    res.append(a[i][0])
                else:
                    raise ValueError()
            else:
                res.append(a[i][:J]+a[i][J+1:])
    return res


# функция считающая определители
def determinant(a):
    if len(a) == 1:
        return float(a[0])
    else:
        sum = 0
        for i in range(len(a[0])):
            sum += float(a[0][i])*((-1)**i)*determinant(minor(a, 0, i))
        return sum


# Ввод матрицы
m = int(input("Введите кол-во строк матрицы "))
matrix = []
mat = []
print("Вводите строки матрицы (enter после каждой строки). Элементы в строке разделяйте пробелами")
for i in range(m):
    b = list(input().split())
    matrix.append(b)
    mat.append([0]*m)


# заполняем матрицу миноров mat
for i in range(len(mat)):
    for k in range(len(mat[0])):
        mat[i][k] = ((-1)**(k + i))*float(determinant(minor(matrix, k, i)))
        mat[i][k] = round((mat[i][k]*(1/determinant(matrix))), 10)

for i in mat:
    print (i)