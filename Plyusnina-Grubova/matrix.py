import permutations


class Matrix:
    def __init__(self, a):
        if len(a) == 0 or len(a[0]) == 0:
            raise ValueError('not a valid matrix: length is 0')
        for row in a:
            if len(row) != len(a[0]):
                raise ValueError('not a valid matrix: row lengths differ')
        self.a = a

    def dim(self):
        return len(self.a), len(self.a[0])

    # Task 1
    def __add__(self, other):
        if self.dim() != other.dim():
            raise ValueError('matrices have different dimensions')
        res = []
        for i in range(len(self.a)):
            res.append([])
            for j in range(len(self.a[0])):
                res[-1].append(self.a[i][j] + other.a[i][j])
        return Matrix(res)

    # Task 1
    def __mul__(self, other):
        if self.dim()[1] != other.dim()[0]:
            raise ValueError('matrices are incompatible for multiplication')
        res = []
        for i in range(len(self.a)):
            res.append([])
            for j in range(len(other.a[0])):
                res[-1].append(0)
                for k in range(len(other.a)):
                    res[-1][-1] += self.a[i][k] * other.a[k][j]
        return Matrix(res)

    # Task 2
    def det(self):
        if self.dim()[0] != self.dim()[1]:
            raise ValueError('matrix is not square')
        res = 0
        for perm in permutations.generate(self.dim()[0]):
            prod = 1
            for i, j in enumerate(perm):
                prod *= self.a[i][j]
            res += prod * ((-1) ** permutations.parity(perm))
        return res

    # Task 2
    def trans(self):
        res = []
        for i in range(len(self.a[0])):
            res.append([])
            for j in range(len(self.a)):
                res[-1].append(self.a[j][i])
        return Matrix(res)

    # Task 2
    def minor(self, i, j):
        res = []
        for ri in range(len(self.a)):
            if ri == i:
                continue
            res.append(self.a[ri][:j] + self.a[ri][j + 1:])
        return Matrix(res)

    # Task 2
    def __invert__(self):
        det, n = self.det(), len(self.a)
        if det == 0:
            raise ValueError('determinant is zero')
        res = []
        trans = self.trans()
        for i in range(n):
            res.append([])
            for j in range(n):
                coef, value = (-1) ** (i + j), trans.minor(i, j).det()
                res[-1].append(coef * value / det)
        return Matrix(res)

    # Task 3
    def characteristic_polynom(self):
        if self.dim()[0] != self.dim()[1]:
            raise ValueError('matrix is not square')
        if self.dim()[0] != 3:
            raise ValueError('size not equal to 3 is not supported')

        coef = [self.det(), 0, 0, -1]
        for i in range(3):
            coef[2] += self.a[i][i]
            coef[1] -= self.a[i][i] * self.a[i - 1][i - 1]
        for i, j in ([0, 1], [0, 2], [1, 2]):
            coef[1] += self.a[i][j] * self.a[j][i]

        s = ''
        for d in range(3, -1, -1):
            if coef[d] == 0:
                continue
            if coef[d] > 0:
                s += '+'
            if abs(coef[d]) != 1:
                s += str(coef[d])
            elif coef[d] < 0:
                s += '-'
            s += 'x' * d
        return s

    def __repr__(self):
        s = ''
        for row in self.a:
            s += ' '.join(map(str, row))
            s += '\n'
        return s


def read_matrix():
    n = int(input('Enter number of rows and matrix itself: '))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    return Matrix(a)


m1 = read_matrix()
# m2 = read_matrix()
# print(m1 + m2)
# print(m1 * m2)

print(~m1)
print(m1 * ~m1)
print(m1.characteristic_polynom())