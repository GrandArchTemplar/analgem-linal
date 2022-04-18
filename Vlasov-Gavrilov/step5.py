def rounds_numbers(x):
    """
    Округляет числа
    :param x: Входное число
    :return Округленное число
    """
    return round(x, 2) if x % 1 != 0.0 else int(x)


def reading_matrix():
    """
    Считывает матрицу
    :return: Начальная матрица
    """
    initMatrix = []
    for i in range(2):
        initMatrix.append(list(map(float, input(f"i={i + 1}: ").split()))[:2])
    return initMatrix


def find_roots(initMatrix):
    """
    Находит корни характеристического уравнения
    :param initMatrix: Начальная матрица
    :return L1, L2: Корни характеристического уравнения
    """
    a = 1
    b = - initMatrix[0][0] - initMatrix[1][1]
    c = initMatrix[0][0] * initMatrix[1][1] - initMatrix[0][1] * initMatrix[1][0]
    D = b ** 2 - 4 * a * c
    if D < 0:
        return False
    elif D == 0:
        L1 = 0
        L2 = (- b - D ** 0.5) / (2 * a)
    else:
        L1 = (- b - D ** 0.5) / (2 * a)
        L2 = (- b + D ** 0.5) / (2 * a)
    return L1, L2


def find_x1_and_x2(initMatrix, L):
    """
    Находит x1 и x2 собственных векторов
    :param initMatrix: Начальная матрица
    :param L: Корень характеристического уравнения
    :return: Координаты x1 и x2
    """
    if L == 0:
        return False
    elif initMatrix[0][1] == 0 and L - initMatrix[0][0] == 0:
        if initMatrix[1][0] == 0 and L - initMatrix[1][1] == 0:
            x1, x2 = 2, 4
        elif initMatrix[1][0] == 0 and L - initMatrix[1][1] != 0:
            x1, x2 = 2, 0
        elif initMatrix[1][0] != 0 and L - initMatrix[1][1] == 0:
            x1, x2 = 0, 4
        else:
            x1 = 2
            x2 = (L - initMatrix[1][1]) * x1 / initMatrix[1][0]
    elif initMatrix[0][1] == 0 and L - initMatrix[0][0] != 0:
        if L - initMatrix[1][1] == 0:
            x1, x2 = 0, 4
        else:
            x1, x2 = 0, 0
    elif initMatrix[0][1] != 0 and L - initMatrix[0][0] == 0:
        if initMatrix[1][0] == 0:
            x1, x2 = 2, 0
        else:
            x1, x2 = 0, 0
    else:
        if initMatrix[1][0] == 0 and L - initMatrix[1][1] == 0:
            x2 = 4
            x1 = initMatrix[0][1] / (L - initMatrix[0][0]) * x2
        elif initMatrix[1][0] != 0 and L - initMatrix[1][1] != 0:
            x1 = 2
            x2 = (L - initMatrix[0][0]) / initMatrix[0][1] * x1
        else:
            x1, x2 = 0, 0
    return x1, x2


def composes_matrix_vectors(initMatrix, L1, L2):
    """
    Составляет матрицу из собственных векторов
    :param initMatrix: Начальная матрица
    :return Матрица собственных векторов
    """
    matrix = [[0, 0], [0, 0]]
    matrix[0][0], matrix[1][0] = find_x1_and_x2(initMatrix, L1)
    matrix[0][1], matrix[1][1] = find_x1_and_x2(initMatrix, L2)
    return matrix


def find_inv_matrix(matrix):
    """
    Находит обратную матрицу
    :param matrix: Матрица собственных векторов
    :return Обратная матрица
    """
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if det == 0:
        return False
    else:
        invMatrix = [[0, 0], [0, 0]]
        invMatrix[0][0], invMatrix[1][0] = matrix[1][1] / det, - matrix[1][0] / det
        invMatrix[1][1], invMatrix[0][1] = matrix[0][0] / det, - matrix[0][1] / det
        return invMatrix


def find_P1_and_P2(matrix, invMatrix):
    """
    Находит P1 и P2
    :param matrix: Матрица собственных векторов
    :param invMatrix: Обратная матрица
    :return P1 и P2
    """
    P1, P2 = [[0, 0], [0, 0]], [[0, 0], [0, 0]]
    P1[0][0], P1[1][0] = matrix[0][0] * invMatrix[0][0], matrix[1][0] * invMatrix[0][0]
    P1[1][1], P1[0][1] = matrix[1][0] * invMatrix[0][1], matrix[0][0] *  invMatrix[0][1]
    P2[0][0], P2[1][0] = matrix[0][1] * invMatrix[1][0], matrix[1][1] * invMatrix[1][0]
    P2[1][1], P2[0][1] = matrix[1][1] * invMatrix[1][1], matrix[0][1] *  invMatrix[1][1]
    return P1, P2

    
def print_matrix(matrix, number):
    """
    Выводит матрицу
    :param matrix: P
    :param number: номер P
    """
    print(f"P{number}:")
    matrixLen = []
    for i, line in enumerate(matrix):
        for j, value in enumerate(line):
            matrix[i][j] = rounds_numbers(matrix[i][j])
            matrixLen.append(len(str(value)))
    maxLen = max(matrixLen)
    for i in range(2):
        print(f"i={i + 1}:", *list(map("{{:>{length}}}".format(length=maxLen).format, matrix[i])))


initMatrix = reading_matrix()
if find_roots(initMatrix):
    L1, L2 = find_roots(initMatrix)
    if find_x1_and_x2(initMatrix, L1) and find_x1_and_x2(initMatrix, L2):
        matrix = composes_matrix_vectors(initMatrix, L1, L2)
        if find_inv_matrix(matrix):
            invMatrix = find_inv_matrix(matrix)
            P1, P2 = find_P1_and_P2(matrix, invMatrix)
            print_matrix(P1, 1)
            print_matrix(P2, 2)
        else:
            print("Определитель матрицы собственных векторов равен нулю")
    else:
        print("Одно или оба собственных значения равен или равны нулю")
else:
    print("Нет рациональных собственных значений")