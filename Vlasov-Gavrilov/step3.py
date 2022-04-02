def reading_matrix():
    """
    Считывает матрицу и записывает ее в двумерный список
    :return: Сформированный список и его длинну
    """
    print("Введите строки матрицы через пробел")
    lst = []
    for i in range(3):
        lst.append(list(map(int, input(f"i = {i + 1}: ").split()))[:3])
    return lst


def print_matrix(lst):
    """
    Выводит матрицу
    :param lst: Входной двумерный список
    """
    print("Ваша матЬрица")
    lst_len = []
    for line_lst in lst:
        for value in line_lst:
            lst_len.append(len(str(value)))
    max_len = max(lst_len)
    for i in range(3):
        print(f"i = {i + 1}:", *list(map("{{:>{length}}}".format(length=max_len).format, lst[i])))


def find_and_print_charact_eq(lst):
    """
    Находит и выводит характеристическое уравнение для матрицы 3x3
    :param lst: Входной двумерный список
    """
    a = - 1
    b = + lst[0][0] + lst[1][1] + lst[2][2]
    c = - lst[0][0] * lst[1][1] - lst[0][0] * lst[2][2] - lst[1][1] * lst[2][2] \
        + lst[0][1] * lst[1][0] + lst[0][2] * lst[2][0] + lst[1][2] * lst[2][1]
    d = + lst[0][0] * lst[1][1] * lst[2][2] + lst[0][1] * lst[1][2] * lst[2][0] + lst[0][2] * lst[1][0] * lst[2][1] \
        - lst[0][2] * lst[1][1] * lst[2][0] - lst[1][2] * lst[0][0] * lst[2][1] - lst[0][1] * lst[2][2] * lst[1][0]
    print("Ваше уравнение")
    for i in a, b, c, d:
        if i == 0:
            continue
        elif i == a:
            print(f"- \u03BB\u00B3", end=" ")
        elif i == b:
            print(f"- {abs(b)}\u03BB\u00B2", end=" ") if b < 0 else print(f"+ {b}\u03BB\u00B2", end=" ")
        elif i == c:
            print(f"- {abs(с)}\u03BB", end=" ") if c < 0 else print(f"+ {c}\u03BB", end=" ")
        else:
            print(f"- {abs(d)}", end=" ") if d < 0 else print(f"+ {d}", end=" ")


matrix = reading_matrix()
print_matrix(matrix)
find_and_print_charact_eq(matrix)
