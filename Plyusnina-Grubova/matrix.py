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
m2 = read_matrix()
# print(m1 + m2)
print(m1 * m2)