A = []
print("Введите данные по строкам слева направо:")
for i in range(2):
    a = []
    for j in range(2):
        a.append(int(input()))
    A.append(a)
print("Матрица:")
for i in range(2):
    for j in range(2):
        print(A[i][j], end=" ")
    print()
print(" ")
a1=A[0][0]
b1=A[0][1]
c1=A[1][0]
d1=A[1][1]
a=1
b=(a1+d1)*(-1)
c=a1*d1-b1*c1
l1=((-1)*b+((b*b-4*a*c)**0.5))/2
l2=((-1)*b-((b*b-4*a*c)**0.5))/2
try:
    try:
        x1=1
        x2=c1*x1/(l1-d1)
        print('число:',l1, 'вектор: [',x1,",", x2,"]")
    except:
        x2=1
        x1=b1*x2/(l1-a1)
        print('число:', l1, 'вектор: [',x1,",", x2,"]")
    try:
        x1=1
        x2=c1*x1/(l2-d1)
        print('число:',l2, 'вектор: [',x1,",", x2,"]")
    except:
        x2=1
        x1=b1*x2/(l2-a1)
        print('число:', l2, 'вектор: [',x1,",", x2,"]")
except:
    print('число:', 0, 'вектор: [',1,",", 0,"]")