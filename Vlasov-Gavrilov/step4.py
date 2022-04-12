def reading_matrix():
    """
    Считывает матрицу и записывает ее в двумерный список
    :param type: Тип элементов
    :return: Сформированный список и его длинну
    """
    lst = []
    for i in range(2):
        lst.append(list(map(float, input(f"i = {i + 1}: ").split()))[:2])
    return lst


def find_roots(lst):
    """
    Находит корни характеристического уравнения для матрицы 2x2
    :param lst: Входной двумерный список
    :return L1, L2: Корни характеристического уравнения
    """
    a = 1
    b = - lst[0][0] - lst[1][1]
    c = lst[0][0] * lst[1][1] - lst[0][1] * lst[1][0]
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


def find_x1_and_x2(lst, L, n):
    """
    Находит x1 и x2 собственных векторов
    :param lst: Входной двумрный список
    :param L: Корень характеристического уравнения
    :param n: Округление
    :return: Координаты x1 и x2
    """
    if L == 0:
        return False
    elif lst[0][1] == 0 and L - lst[0][0] == 0:
        if lst[1][0] == 0 and L - lst[1][1] == 0:
            x1, x2 = 1, 1
        elif lst[1][0] == 0 and L - lst[1][1] != 0:
            x1, x2 = 1, 0
        elif lst[1][0] != 0 and L - lst[1][1] == 0:
            x1, x2 = 0, 1
        else:
            x1 = 1
            x2 = (L - lst[1][1]) * x1 / lst[1][0]
    elif lst[0][1] == 0 and L - lst[0][0] != 0:
        if L - lst[1][1] == 0:
            x1, x2 = 0, 1
        else:
            x1, x2 = 0, 0
    elif lst[0][1] != 0 and L - lst[0][0] == 0:
        if lst[1][0] == 0:
            x1, x2 = 1, 0
        else:
            x1, x2 = 0, 0
    else:
        if lst[1][0] == 0 and L - lst[1][1] == 0:
            x2 = 1
            x1 = lst[0][1] / (L - lst[0][0]) * x2
        elif lst[1][0] != 0 and L - lst[1][1] != 0:
            x1 = 1
            x2 = (L - lst[0][0]) / lst[0][1] * x1
        else:
            x1, x2 = 0, 0
    return round(x1, n), round(x2, n)


def print_winds():
    """
    Выводит собственные вектора
    """
    lst = reading_matrix()
    n = int(input("Введите до какого знака округлять: "))
    if find_roots(lst):
        L1, L2 = find_roots(lst)
        if find_x1_and_x2(lst, L1, n):
            print(f"\u03BB1={round(L1, n)} {list(find_x1_and_x2(lst, L1, n))}")
        else:
            print("\u03BB1=0")
        if find_x1_and_x2(lst, L2, n):
            print(f"\u03BB2={round(L2, n)} {list(find_x1_and_x2(lst, L2, n))}")
        else:
            print("\u03BB2=0")
    else:
        print("Нет вещественных собственных значений")


print_winds()