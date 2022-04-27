from tabulate import tabulate


def input_n_matrix(number):
    n = input(f'\nВведите количество строк в матрице {number} (без пробелов): ')
    if n.isdigit() and int(n) != 0:
        print(f'Введите матрицу {number} построчно: значения в строке через пробелы, переход на следующую строку через enter:')
        try:
            matrix = [[i for i in list(map(float, input().split()))] for _ in range(int(n))]
            k = 0
            for i in matrix:
                if len(i) != max([len(i) for i in matrix]):
                    k += 1
            if k != 0:
                print('Строки разной длины. Попробуйте еще раз!\n')
                operations()
            else:
                return matrix
        except ValueError:
            print('Что-то пошло не так... Мы не умеем работать с нечисловыми матрицами. Попробуйте еще раз!\n')
            operations()
    else:
        print('Введено не целое положительное число, это не логично. Попробуйте еще раз!\n')
        operations()


def adder():
    matrix1 = input_n_matrix(1)
    matrix2 = input_n_matrix(2)
    if len(matrix1[0]) != len(matrix2[0]) or len(matrix1) != len(matrix2):
        print('Сори, матрицы разного размера не складываются. Попробуйте еще раз!\n')
        adder()
    else:
        matrix = matrix1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] += matrix2[i][j]
        print('\nОтвет:\n' + tabulate(matrix, tablefmt="plain"))


def multiplier():
    matrix1 = input_n_matrix(1)
    matrix2 = input_n_matrix(2)
    if len(matrix1[0]) != len(matrix2):
        print('Сори, матрицы таких размеров не умножаются. Попробуйте еще раз!\n')
        multiplier()
    else:
        matrix = [[0 for i in range(len(matrix1))] for j in range(len(matrix2[0]))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix1[0])):
                    matrix[i][j] += matrix1[i][k] * matrix2[k][j]
        print('\nОтвет:\n' + tabulate(matrix, tablefmt="plain"))


def operations():
    action = input('\nВведите * для умножения матриц, + для сложения: ')
    if action == '*':
        multiplier()
    elif action == '+':
        adder()
    else:
        print('Что вы хотите? Определитесь, пожалуйста, и попробуйте еще раз!\n')
        operations()


operations()

answer = input('\nЕсли хотите продолжить, введите Y\n')
if answer == 'Y':
    print()
    operations()
