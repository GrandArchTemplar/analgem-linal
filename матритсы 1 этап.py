def clozhenie(m1, m2):
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):  # проверка на совпадение размеров матриц
        print('Извините, я так не умею (никто не умеет)')
    else:
        m = m1
        for i in range(len(m1)):
            for j in range(len(m1[0])):
                m[i][j] += m2[i][j]
        print(m)


def multiplication(m1, m2):
    if len(m1[0]) != len(m2):
        print('Павел Андреевич вы дебил')
    else:
        matritsa = [[0] * len(m1) for i in range(len(m2[0]))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                s = 0
                for k in range(len(m2)):
                    s += m1[i][k] * m2[k][j]
                    matritsa[i][j] = s
        print(matritsa)


def what(matrices):  # функция, спрашивающая что дальше делать с этими вашими матрицами
    def print_m(m):  # функция вывода матриц на экран
        for i in m: print(i)
        print()  # чтоб отступ в конце был

    while True:  # зациклили, чтобы после выполнения одной операции тут же предлагалось выполнить другую
        v = int(input(
            'Введите "1" если хотите сложить матрицы, введите "2" если хотите умножить их, и "3" если хотите их вывести на экран)))0))000 '))
        if v == 1:  # сложение получается
            clozhenie(matrices[0], matrices[1])
        elif v == 2:  # умножение получается
            multiplication(matrices[0], matrices[1])
        elif v == 3:  # просто выводим матрицы на экран
            print_m(matrices[0])
            print_m(matrices[1])
        else:
            print('Павел Андреевич, вы еблан!')


def inputMatrices():
    def do_matrix_please(n):  # составим матрицы по введённым размерам, вернём tuple из двух получившихся матриц
        print('Введите вашу матрицу построчно через пробелы')
        while True:
            try:
                matrix = [[i for i in list(map(int, input().split()))] for j in range(n)]
                break  # как только всё пройдёт без ошибок, мы выйдем из цикла
            except ValueError:
                print('Зачем вы вводите буковки/символы/пробелы?? Попробуйте ещё раз!)')
        max_len = max([len(i) for i in matrix])  # это длина самой длинной строки в матрице
        for i in matrix:
            if len(i) != max_len:  # если вдруг длина введённых пользователем строк оказалось разной
                i.extend([0 for i in range(max_len - len(i))])  # добавляем столько ноликов, сколько не хватает
        return matrix

    def input_n(number):  # чтобы избежать ошибки из-за введённой буквы вместо цифры
        flag = True
        while flag == True:
            try:
                n = int(input(f'Сколько строк будет матрице {number}? '))  # число строк матрицы
                flag = False
            except:
                print('Зачем вы вводите буковки/символы/пробелы?? Попробуйте ещё раз!)')
        return n

    m1 = do_matrix_please(input_n(1))
    m2 = do_matrix_please(input_n(2))
    return (m1, m2)


def main():  # главная функция
    what(inputMatrices())


main()
