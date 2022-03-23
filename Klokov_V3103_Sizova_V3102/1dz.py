"""Задание 1"""
import sys
n1=int(input('количество строк матрицы 1'))
m1=int(input('количество столбцов матрицы 1'))
mat1=[[0]*m1 for _ in range(n1)]
for i in range(n1):
    mat1[i]=input().split()
n2 = int(input('количество строк матрицы 2'))
m2=int(input('количество столбцов матрицы 2'))
mat2 = [[0] * m2 for _ in range(n2)]
for i in range(n2):
    mat2[i] = input().split()
z=input('+ или *?????')
if z=='+':
    mat = [[0] * m1 for _ in range(n1)]
    if n1==n2 and m1==m2:
        for i in range(n1):
            for j in range(m1):
                mat[i][j]=int(mat1[i][j])+int(mat2[i][j])
    else: sys.exit()
if z=='*':
    mat = [[0] * m2 for _ in range(n1)]
    if m1==n2:
        for i in range(n1):
            for j in range(m2):
                for k in range(m1):
                    mat[i][j] += int(mat1[i][k])*int(mat2[k][j])
    else: sys.exit()
for i in range(n1):
    print(mat[i])
# 5 3 6 5 8 4 5
# 7 4 5 6 2 7 5