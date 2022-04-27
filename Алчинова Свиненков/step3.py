def input_matrix3x3():
    print('\nВведите матрицу 3х3 построчно: значения в строке через пробелы, переход на следующую строку через enter.')
    try:
        matrix = [[i for i in list(map(float, input().split()))] for _ in range(3)]
        k = 0
        for i in matrix:
            if len(i) != max([len(i) for i in matrix]):
                k += 1
        if k != 0:
            print('Строки разной длины. Попробуйте еще раз!\n')
            input_matrix3x3()
        else:
            if len(matrix) != len(matrix[0]):
                print(
                    'Сори, мы ищем характеристические уравнения только для квадратных матриц 3x3. Попробуйте еще раз!\n')
                input_matrix3x3()
            else:
                return matrix
    except ValueError:
        print('Что-то пошло не так... Мы не умеем работать с нечисловыми матрицами. Попробуйте еще раз!\n')
        input_matrix3x3()


def hi_lambda():
    matrix = input_matrix3x3()
    A = '-xxx '
    b = matrix[0][0] + matrix[1][1] + matrix[2][2]
    if b > 0:
        B = f'+ {b}xx '
    elif b == 0:
        B = ''
    else:
        B = f'- {-b}xx '
    c = matrix[0][1] * matrix[1][0] + matrix[0][2] * matrix[2][0] + matrix[1][2] * matrix[2][1] \
        - matrix[0][0] * matrix[1][1] - matrix[0][0] * matrix[2][2] - matrix[1][1] * matrix[2][2]
    if c > 0:
        C = f'+ {c} '
    elif c == 0:
        C = ''
    else:
        C = f'- {-c} '
    d = matrix[0][0] * matrix[1][1] * matrix[2][2] + matrix[0][1] * matrix[1][2] * matrix[2][0] \
        + matrix[0][2] * matrix[2][1] * matrix[1][0] - matrix[0][2] * matrix[1][1] * matrix[2][0] \
        - matrix[0][0] * matrix[1][2] * matrix[2][1] - matrix[0][1] * matrix[2][2] * matrix[1][0]
    if d > 0:
        D = f'+ {d} '
    elif d == 0:
        D = ''
    else:
        D = f'- {-d} '
    print(f'\nОтвет: {A}{B}{C}{D}= 0')


hi_lambda()

answer = input('\nЕсли хотите продолжить, введите Y\n')
if answer == 'Y':
    print()
    hi_lambda()
