strok = (int(input('Введите количество строк ')))
eliments = (int(input("Введите количество элементов в строке  ")))
if strok != eliments:
    print("Матрица кривая не квадратная")
else:
    A = []  # матрица
    s = 0  # счетчик строк
    c = 0  # счетчик элементов в строке
    while s < strok:  # создает строки
        a = []
        c = 0
        p = 0
        if s > 0:
            print("Cледующая строка ")
        while c < eliments:  # элементы в строках
            p = float(input("Введите число в строке "))
            a.insert(c, p)
            c += 1
        s += 1
        A.insert(s, a)

def det(A, total=0):
    indices = list(range(len(A)))

    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
    for fc in indices:  # Ищем микроматрицы для каждого того что вычеркнули
        As = A
        As = As[1:]  # -1 строка
        height = len(As)  # колличество строк
        for i in range(height):
            # убираем столбцы
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)  # чередуем знаки
        # рекурсия
        sub_det = det(As)
        # складываем
        total += sign * A[0][fc] * sub_det
    return total
# ищем минор
def minor(lst, i, j):
    LST = []
    n = len(lst)
    for k in range(n):
        for s in range(n):
            if k != i and s != j:
                LST.append(lst[k][s])
    minor = []
    m = len(LST)
    for p in range(0, m, n - 1):
        minor.append(LST[p: p + n - 1])
    return minor

def minor_matr(A):
    Mij = 0
    M = [[0 for i in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A)):
            if len((minor(A, i, j))) >= 2:
                Mij = det(minor(A, i, j))
                M[i][j] = Mij * ((-1) ** (i+j))
            else:
                Mij = minor(A, i, j)[0][0]
                M[i][j] = Mij * ((-1) ** (i+j))
    return M

#ранспониру.
def zeros_matrix(rows, cols):
# МАТРИЦА НУЛЕЙ РОВС СТРОКИ КОЛС СТОЛБЫ
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M

def transpose(M):
# отражаем относительно диагонали транспонируем
    # делаем двумерный список если он не такой
    if not isinstance(M[0], list):
        M = [M]
    # столбы и строки опредялем
    rows = len(M)
    cols = len(M[0])
    #  MT транспонируема матрица размеры как у исзодной
    MT = zeros_matrix(cols, rows)
    # транспонируем копируем переносим отражаем
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT

def END(A):
    M = [[0 for i in range(len(A))] for i in range(len(A))]
    if det(A) == 0:
        print("")
    else:
        M = [[0 for i in range(len(A))] for i in range(len(A))]
        P = transpose(minor_matr(A))
        for i in range(len(A)):
            for j in range(len(A)):
                M[i][j] = P[i][j]/det(A)
    return M
if END(A) == transpose(A):
    print('Унитарная')
else:
    print("Неунитарная")
if transpose(A) == A:
    print("самосопряженная")
else:
    print("не самосопряженная")