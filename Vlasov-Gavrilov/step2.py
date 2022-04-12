import copy


def reading_matrix():
    """
    Считывает матрицу и записывает ее в двумерный список
    :return: Сформированный список и его длинну
    """
    n = int(input("Введите размер вашей матрицы (число): "))
    lst = []
    for i in range(n):
        lst.append(list(map(float, input(f"Введите строку номер {i + 1} (элементы через пробел): ").split())))
    return lst


def transposes_matrix(lst):
    """
    Транспонирует матрицу
    :param lst: Входной двумерный список
    :return: Сформированный транспонированный список и его длинну
    """
    n = len(lst)
    for i in range(n):
        for j in range(i, n):
            lst[i][j], lst[j][i] = lst[j][i], lst[i][j]
    return lst


def find_det(lst):
    """
    Находит определитель переданной матрицы
    :param lst: Входной двумерный список - матрица
    :return: Определитель
    """
    n = len(lst)
    if n == 1:
        return lst[0][0]
    else:
        det = 0
        for k in range(n):
            det += lst[0][k] * find_alg_compl(lst, 0, k)
        return det


def find_minor(lst, i, j):
    """
    Находит минор для элемента с индексами i и j
    :param lst: Входной двумерный список
    :param i: i
    :param j: j
    :return: Двумерный список - минор
    """
    minor = copy.deepcopy(lst)
    n = len(minor)
    for k in range(n):
        del (minor[k][j])
    del (minor[i])
    return minor


def find_alg_compl(lst, i, j):
    """
    Находит алгебраическое дополнение для элемента с индексами i и j
    :param lst: Входной двумерный список
    :param i: i
    :param j: j
    :return: Алгебраическое дополнение
    """
    minor = find_minor(lst, i, j)
    alg_compl = (-1) ** (i + j) * find_det(minor)
    return alg_compl


def find_inv_matrix(lst):
    """
    Находит обратную матрицу к переданной матрице - двумерному списку
    :param lst: Входной двумерный список
    :return: Обратная матрица - двумерный список
    """
    n = len(lst)
    m = len(lst[0])
    round_up = int(input("Введите до какого знака округлять: "))
    for line_lst in lst:
        if len(line_lst) != m:
            return "Почему строки разной длины?"
    if n != m:
        return "Почему матрица не квадратная?"
    elif find_det(lst) == 0:
        return "Определитель равен 0 - найти обратную матрицу не получится :("
    else:
        transp_lst = transposes_matrix(lst)
        LST = []
        for i in range(n):
            line_LST = []
            for j in range(n):
                value = find_alg_compl(transp_lst, i, j) / find_det(lst)
                line_LST.append(round(value, round_up) if value % 1 != 0.0 else int(value))
            LST.append(line_LST)
        return LST


def print_matrix(LST):
    """
    Выводит матрицу
    :param LST: Входной двумерный список
    """
    if type(LST) != list:
        print(LST)
    else:
        print("Обратная матрица: ")
        max_len = max([len(str(value)) for line_LST in LST for value in line_LST])
        for line_LST in LST:
            print(*list(map('{{:>{length}}}'.format(length=max_len).format, line_LST)))


print_matrix(find_inv_matrix(reading_matrix(), round_up=int(
    input("Введите желаемое количество знаков после запятой у результата (число): "))))
