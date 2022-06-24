from matrix import Matrix

# Task 7
Matrix.FORMATTER = lambda value: f'{value:.3f}'

n = int(input())
a = []
for i in range(n):
    v = list(map(int, input().split()))
    a.append(Matrix([v]))


def cross_product(u, v):
    return (u * v.trans()).a[0][0]


b = []
for i in range(n):
    v = a[i]
    for j in range(i):
        proj = b[j] * (cross_product(a[i], b[j]) / cross_product(b[j], b[j]))
        v = v + proj * (-1)
    b.append(v)

for i in range(n):
    print(b[i], end='')

# Check
print('Check:')
a = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        a[i][j] = cross_product(b[i], b[j])
print(Matrix(a))  # Should have non-zeroes only on main diagonal
