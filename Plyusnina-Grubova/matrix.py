import permutations
from math import sqrt
from numbers import Number


class Matrix:
    FORMATTER = str

    def __init__(self, a):
        if len(a) == 0 or len(a[0]) == 0:
            raise ValueError('not a valid matrix: length is 0')
        for row in a:
            if len(row) != len(a[0]):
                raise ValueError('not a valid matrix: row lengths differ')
        self.a = a

    def dim(self):
        return len(self.a), len(self.a[0])

    def __eq__(self, other):
        return self.a == other.a

    @staticmethod
    def one(n):
        return Matrix([[1 if i == j else 0 for j in range(n)]
                       for i in range(n)])

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

    def __mul__(self, other):
        # Task 1
        if isinstance(other, Matrix):
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
        # Task 5
        elif isinstance(other, Number):
            res = []
            for i in range(len(self.a)):
                res.append([])
                for j in range(len(self.a[0])):
                    res[-1].append(self.a[i][j] * other)
            return Matrix(res)
        else:
            raise ValueError('unsupported multiplication')

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

    # Task 4
    def eigenvalues(self):
        if self.dim()[0] != self.dim()[1]:
            raise ValueError('matrix is not square')
        if self.dim()[0] != 2:
            raise ValueError('size not equal to 2 is not supported')

        coef = [-self.a[0][0] - self.a[1][1], self.det()]
        d = coef[0] ** 2 - 4 * coef[1]
        if d < 0:
            return []
        elif d == 0:
            return [-coef[0] / 2]
        else:
            return [(-coef[0] + sqrt(d)) / 2, (-coef[0] - sqrt(d)) / 2]

    # Task 4
    def eigenpairs(self):
        values = self.eigenvalues()
        res = []
        for c in values:
            if self.a[0][1] != 0:
                v = [1, (c - self.a[0][0]) / self.a[0][1]]
            elif self.a[1][0] != 0:
                v = [(c - self.a[1][1]) / self.a[1][0], 1]
            elif self.a[0][0] == c:
                v = [1, 0]
            elif self.a[1][1] == c:
                v = [0, 1]
            else:
                assert False  # should be impossible
            res.append((c, v))
        return res

    # Task 5
    def projectors(self):
        pairs = self.eigenpairs()
        if len(pairs) == 2:
            res = []
            for i in range(2):
                ci, cj = pairs[i][0], pairs[i - 1][0]
                m = self + Matrix([[-cj, 0], [0, -cj]])
                res.append(m * (1 / (ci - cj)))
            return res
        elif len(pairs) == 1:
            c, v = pairs[0]
            m = Matrix([v, [0, 0]])
            return [m.trans()]
        else:
            return []

    # Task 6
    def is_unitary(self):
        if self.dim()[0] != self.dim()[1]:
            return False
        # Assuming we don't work with complex numbers,
        # so it's just transpose instead of conjugate transpose
        return self * self.trans() == Matrix.one(self.dim()[0])

    def is_self_conjugated(self):
        # Again, assuming we don't work with complex numbers
        return self == self.trans()

    def __repr__(self):
        s = ''
        for row in self.a:
            s += ' '.join(map(Matrix.FORMATTER, row))
            s += '\n'
        return s


def read_matrix():
    n = int(input('Enter number of rows and matrix itself: '))
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    return Matrix(a)


TASKS = [6, 7]
if __name__ == '__main__':
    m1 = read_matrix()

    if 1 in TASKS:
        m2 = read_matrix()
        print(m1 + m2)  # Task 1
        print(m1 * m2)  # Task 1

    if 2 in TASKS:
        print(~m1)  # Task 2
        print('Check:')
        print(m1 * ~m1)  # Correctness check, should be E

    if 3 in TASKS:
        print(m1.characteristic_polynom())  # Task 3

    if 4 in TASKS:
        ep = m1.eigenpairs()  # Task 4
        for c, v in ep:
            print(c, v)

    if 5 in TASKS:
        proj = m1.projectors()  # Task 5
        for p in proj:
            print(p)

    if 6 in TASKS:
        uni = m1.is_unitary()
        print('Унитарная' if uni else 'Не унитарная')
        sc = m1.is_self_conjugated()
        print('Самосопряженная' if sc else 'Не самосопряженная')
