from tabulate import tabulate


def input_matrix():
    n = input('\nВведите количество строк в квадратной матрице (без пробелов): ')
    if n.isdigit() and int(n) != 0:
        print('Введите квадратную матрицу построчно: значения в строке через пробелы, переход на следующую строку через enter:')
        try:
            matrix = [[i for i in list(map(float, input().split()))] for _ in range(int(n))]
            k = 0
            for i in matrix:
                if len(i) != max([len(i) for i in matrix]):
                    k += 1
            if k != 0:
                print('Строки разной длины. Попробуйте еще раз!\n')
                input_matrix()
            else:
                return matrix
        except ValueError:
            print('Что-то пошло не так... Мы не умеем работать с нечисловыми матрицами. Попробуйте еще раз!\n')
            input_matrix()
    else:
        print('Введено не целое положительное число, это не логично. Попробуйте еще раз!\n')
        input_matrix()


def minor(matrix, i, j):
    return [line[:j] + line[j + 1:] for line in (matrix[:i] + matrix[i + 1:])]


def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0][0]
    else:
        sign = 1
        result = 0
        for j in range(len(matrix)):
            result += sign * matrix[0][j] * determinant(minor(matrix, 0, j))
            sign *= -1
        return result


def alg_add_matrix(matrix):
    result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if (i + j) % 2 != 0:
                result[i][j] = -1 * determinant(minor(matrix, i, j))
            else:
                result[i][j] = determinant(minor(matrix, i, j))
    return result


def transpose_matrix(matrix):
    result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            result[i][j] = matrix[j][i]
    return result


def inverse_matrix():
    matrix = input_matrix()
    if len(matrix) != len(matrix[0]):
        print('Сори, мы ищем обратные матрицы только для квадратных матриц. Попробуйте еще раз!\n')
        inverse_matrix()
    else:
        det_matrix = determinant(matrix)
        if det_matrix == 0:
            print('Обратной матрицы не существует, так как определитель равен нулю. Попробуйте еще раз!\n')
            inverse_matrix()
        else:
            result = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
            for i in range(len(matrix[0])):
                for j in range(len(matrix)):
                    result[i][j] = transpose_matrix(alg_add_matrix(matrix))[i][j]/det_matrix
            print('\nОтвет:\n' + tabulate(result, tablefmt="plain"))


inverse_matrix()

answer = input('\nЕсли хотите продолжить, введите Y\n')
if answer == 'Y':
    print()
    inverse_matrix()
