A=[]
print("Введите данные по строкам слева направо:")
for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    A.append(a)
print("матрица:")
for i in range(3):
    for j in range(3):
        print(A[i][j], end=" ")
    print()
print(" ")
a1=A[0][0]
b1=A[0][1]
c1=A[0][2]
d1=A[1][0]
e1=A[1][1]
f1=A[1][2]
g1=A[2][0]
h1=A[2][1]
i1=A[2][2]

X=-1
Y=a1+e1+i1
Z=c1*g1+b1*d1+f1*h1-e1*a1-a1*i1-e1*i1
W=b1*f1*g1+c1*d1*h1+e1*a1*i1-b1*d1*i1-e1*c1*g1-a1*f1*h1
if Y>=0:
    Y='+'+str(Y)
if Z>=0:
    Z='+'+str(Z)
if W>=0:
    W='+'+str(W)
print(" ")
print("уравнение:")
print(X,'xxx', Y,'xx', Z,'x', W, sep='')