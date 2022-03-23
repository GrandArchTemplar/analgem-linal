"""Задание 3"""
A=[[0]*3 for _ in range(3)]
for i in range(3):
    A[i]=[int(x) for x in input().split()]

"""det=(A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[1][0]*A[2][1]*A[0][2])-(A[0][2]*A[1][1]*A[2][0]+A[0][1]*A[1][0]*A[2][2]+A[1][2]*A[2][1]*A[0][0])
"""
a1=A[0][0]
b1=A[0][1]
c1=A[0][2]
d1=A[1][0]
e1=A[1][1]
f1=A[1][2]
g1=A[2][0]
h1=A[2][1]
i1=A[2][2]

a=-1
b=a1+e1+i1
c=c1*g1+b1*d1+f1*h1-e1*a1-a1*i1-e1*i1
d=b1*f1*g1+c1*d1*h1+e1*a1*i1-b1*d1*i1-e1*c1*g1-a1*f1*h1
"""p=(3*a*c-(b*b))/(3*a*a)
q=(2*b*b*b-9*a*b*c+27*a*a*d)/(27*a*a*a)
const1=(q*(-0.5)+sqrt(q*q/4+p*p*p/27))**(1/3)
x1"""
if b>=0:
    b='+'+str(b)
if c>=0:
    c='+'+str(c)
if d>=0:
    d='+'+str(d)
for i in range(3):
    print(A[i])
print(a,'xxx', b,'xx', c,'x', d, sep='')