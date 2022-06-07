def rounds_numbers(lst):
    """
    Округляет числа
    :param lst: Входной список чисел
    :return Список округленных чисел
    """
    for i, value in enumerate(lst):
        if value % 1 != 0.0:
            lst[i] = round(value, 2)
        else:
            lst[i] = int(value)
    return lst


def reading_lst_a_and_n():
    """
    Считывает координаты векторов и записывает их в
    двумерный список
    :return: Сформированный список и его длинну
    """
    n = int(input("n (число): "))
    lst_a = []
    for i in range(n):
        lst_a.append(list(map(
            float, input(f"a{i + 1} (через пробел): ").split())))
    return lst_a, n


def find_lambda(a, b, n):
    """
    Находи лямду для векторов a и b
    :param a: Входной вектор a
    :param b: Входной вектор b
    :param n: Количество координат у векторов
    :return: Лямду
    """
    pr_aa = []
    pr_bb = []
    for i in range(n):
        pr_aa.append(a[i] * b[i])
        pr_bb.append(b[i] * b[i])
    return sum(pr_aa) / sum(pr_bb)


def find_b(lst_a, lst_b, n, m):
    """
    Находит координаты заданного вектора b
    :param lst_a: Входной список векторов a
    :param lst_b: Входной список векторов b
    :param n: n
    :param m: m
    :return: Список
    """
    lst_b_doner = []
    for i in range(n):
        lst_b_doner.append(
            lst_a[m][i] - sum([find_lambda(
                lst_a[m], lst_b[j], n) * lst_b[j][i] for j in range(m)]))
    return lst_b_doner


def find_lst_b():
    """
    Находит список векторов b
    :return: Список
    """
    lst_a, n = reading_lst_a_and_n()
    lst_b = []
    for m in range(n):
        lst_b.append(find_b(lst_a, lst_b, n, m))
    return lst_b


def print_lst_b():
    """
    Выводит результат на экран
    """
    lst_b = find_lst_b()
    for i, value in enumerate(lst_b):
        value = " ".join(map(str, rounds_numbers(value)))
        print(f"b{i + 1}: {value}")


print_lst_b()
