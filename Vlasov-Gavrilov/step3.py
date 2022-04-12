def reading_matrix():
    """
    Считывает матрицу и записывает ее в двумерный список
    :return: Сформированный список и его длинну
    """
    LST = []
    for i in range(3):
        lst = []
        lst_val = list(map(float, input(f"i = {i + 1}: ").split()))[:3]
        for j in range(3):
            value = lst_val[j]
            lst.append(value if value % 1 != 0.0 else int(value))
        LST.append(lst)
    return LST


def print_matrix(lst):
    """
    Выводит матрицу
    :param lst: Входной двумерный список
    """
    print("Ваша матрица")
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
    round_up = int(input("Введите до какого знака округлять: "))
    a = - 1
    b = + lst[0][0] + lst[1][1] + lst[2][2]
    c = - lst[0][0] * lst[1][1] - lst[0][0] * lst[2][2] - lst[1][1] * lst[2][2] \
        + lst[0][1] * lst[1][0] + lst[0][2] * lst[2][0] + lst[1][2] * lst[2][1]
    d = + lst[0][0] * lst[1][1] * lst[2][2] + lst[0][1] * lst[1][2] * lst[2][0] + lst[0][2] * lst[1][0] * lst[2][1] \
        - lst[0][2] * lst[1][1] * lst[2][0] - lst[1][2] * lst[0][0] * lst[2][1] - lst[0][1] * lst[2][2] * lst[1][0]
    print("Ваше уравнение")
    i = 0
    for value in a, b, c, d:
        value = round(value, round_up) if value % 1 != 0.0 else int(value)
        if value == 0:
            continue
        elif i == 0:
            print(f"- \u03BB\u00B3", end=" ")
        elif i == 1:
            print(f"- {abs(value)}\u03BB\u00B2", end=" ") if value < 0 else print(f"+ {value}\u03BB\u00B2", end=" ")
        elif i == 2:
            print(f"- {abs(value)}\u03BB", end=" ") if value < 0 else print(f"+ {value}\u03BB", end=" ")
        else:
            print(f"- {abs(value)}", end=" ") if value < 0 else print(f"+ {value}", end=" ")
        i += 1


matrix = reading_matrix()
print_matrix(matrix)
find_and_print_charact_eq(matrix)
