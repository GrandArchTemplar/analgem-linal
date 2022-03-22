log = input('Введите * для умножения, + для сложения: ')
if log == '*':
    logg = 1
    print(logg)
elif log == '+':
    logg = 0
    print(logg)
else: print('Чего ты от меня хочешь?')
#ввод первой матрицы
a=int(input('Введите количество строк '))
cum = []
for i in range(a):
    cum.append(list(map(int, input('Через пробелы... ').split())))
print(cum)
# ввод второй матрицы
b=int(input('Введите количество строк '))
ing = []
for i in range(b):
    ing.append(list(map(int, input('Через пробелы... ').split())))
print(ing)
if logg == 0:
    if b==a:
        A = cum
        B = ing
        F = [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
        for i in range(0, len(F)):
            for i2 in range(0, len(F[i])):
                print(F[i][i2], end=' ')
            print()
    else: print('Матрица неподходящих размеров')
elif logg == 1:
    s=0     # сумма
    t=[]    # временная матрица
    C=[] # конечная матрица
    if len(cum)!=len(ing[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1=len(cum) # количество строк в первой матрице
        c1=len(cum[0]) # Количество столбцов в 1
        r2=c1           # и строк во 2ой матрице
        c2=len(ing[0])  # количество столбцов во 2ой матрице
        for z in range(0,r1):
            for j in range(0,c2):
                for i in range(0,c1):
                    s=s+cum[z][i]*ing[i][j]
                t.append(s)
                s=0
            C.append(t)
            t=[]
    for i in range(0, len(C)):
        for i2 in range(0, len(C[i])):
            print(C[i][i2], end=' ')
        print()