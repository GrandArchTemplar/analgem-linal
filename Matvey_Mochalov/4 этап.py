strok = 2
eliments = 2
A = []  # матрица
s = 0  # счетчик строк
c = 0  # счетчик элементов в строке
while s < strok:  # создает строки
    a = []
    c = 0
    p = 0
    if s > 0:
        print("Cледующая строка ")
    while c < eliments:  # элементы в строках
        p = float(input("Введите число в строке "))
        a.insert(c, p)
        c += 1
    s += 1
    A.insert(s, a)
a1 = A[0][0]
b1 = A[0][1]
c1 = A[1][0]
d1 = A[1][1]
a = 1
b = (a1+d1)*(-1)
c = a1*d1-b1*c1
l1 = ((-1)*b+((b*b-4*a*c)**0.5))/2
l2 = ((-1)*b-((b*b-4*a*c)**0.5))/2
try:
    try:
        x1 = 1
        x2 = c1*x1/(l1-d1)
        print('число',l1, 'вектор',x1, x2)
    except:
        x2 = 1
        x1 = b1*x2/(l1-a1)
        print('число', l1, 'вектор', x1, x2)
    try:
        x1 = 1
        x2 = c1*x1/(l2-d1)
        print('число',l2, 'вектор',x1, x2)
    except:
        x2 = 1
        x1 = b1*x2/(l2-a1)
    print('число', l2, 'вектор', x1, x2)
except:
    print('число', 0, 'вектор', 1, 0)