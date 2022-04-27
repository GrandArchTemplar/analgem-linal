from math import sqrt


def input_matrix2x2():
    print('\nВведите матрицу 2x2 построчно: значения в строке через пробелы, переход на следующую строку через enter.')
    try:
        matrix = [[i for i in list(map(float, input().split()))] for _ in range(2)]
        k = 0
        for i in matrix:
            if len(i) != max([len(i) for i in matrix]):
                k += 1
        if k != 0:
            print('Строки разной длины. Попробуйте еще раз!\n')
            input_matrix2x2()
        else:
            if len(matrix) != len(matrix[0]):
                print('Сори, мы ищем собственные значения/вектора только для квадратных матриц 2x2. Попробуйте еще раз!\n')
                input_matrix2x2()
            else:
                return matrix
    except ValueError:
        print('Что-то пошло не так... Мы не умеем работать с нечисловыми матрицами. Попробуйте еще раз!\n')
        input_matrix2x2()


def eigen():
    matrix = input_matrix2x2()
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    lambdas = []

    discriminant = (a - d) ** 2 + 4 * b * c
    if discriminant > 0:
        lambdas.append((a + d + sqrt(discriminant)) / 2)
        lambdas.append((a + d - sqrt(discriminant)) / 2)
    elif discriminant == 0:
        lambdas.append((a + d) / 2)
    else:
        print('Дискриминант меньше нуля, сори, рациональных корней нет. Попробуйте еще раз!\n')
        eigen()

    print('\nОтвет:')
    for item in lambdas:
        try:
            vector = (1.0, (item - a) / b)
        except ZeroDivisionError:
            if a == item:
                try:
                    vector = (1.0, c / (item - d))
                except ZeroDivisionError:
                    if c == 0:
                        vector = 'любой'
                    else:
                        vector = (0.0, 1.0)
            else:
                vector = (0.0, 1.0)
        print(f'Собственное значение = {item}, собственный вектор = {vector}')


eigen()

answer = input('\nЕсли хотите продолжить, введите Y\n')
if answer == 'Y':
    print()
    eigen()
