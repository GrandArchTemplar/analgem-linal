def multi(C, B):
    multi = [[0 for i in range(len(C))] for j in range(len(C[0]))]
    for i in range(len(C)):
        for j in range(len(B[0])):
            for r in range(len(C[0])):
                multi[i][j] += C[i][r] * B[r][j]
    return multi


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def sym(M):
    for i in range(len(M)):
        for j in range(i):
            if M[i][j] != M[j][i]:
                return False
    return True

# Матрица А размера n*n
n = int(input('Какой размер матрицы А? '))
print('Ввод матрицы А:')
A = [list(map(float, input().split())) for i in range(n)]
m = len(A[0])
E = [[1 if j == i else 0 for i in range(len(A))] for j in range(len(A[0]))]
print(A)
# Проверка матрицы  А
for i in range(len(A)):
    if m != n or m != len(A[i]):
        print('Матрица некорректна')
        exit(0)


if multi(A, transpose(A)) == E:
    print('унитарная')
    if A == transpose(A):
        print('самосопряженная')
    else:
        print('не самосопряженная')
else:
    print('не унитарная')
    if sym(A):
        print('самосопряженная')
    else:
        print('не самосопряженная')
