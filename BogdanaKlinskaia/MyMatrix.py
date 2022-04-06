import sys


class MyMatrix:
    @staticmethod
    def read_matrix(input=sys.stdin, output=sys.stdout, erroutput=sys.stderr):
        print(
            "Введите кол-во строк (целое число) в матрице, нажмите eneter, затем введите строки матрицы, разделяя столбцы пробелом, а строки enter-ом:",
            file=output)
        n = int(input.readline().strip())
        matrix = []
        matrix.append(list(map(float, input.readline().strip().split())))
        m = len(matrix[0])
        for i in range(1, n):
            t = list(map(float, input.readline().strip().split()))
            while len(t) != m:
                print(
                    f"Что-то пошло не так, должно быть {m} элементов в строке, а получлось {len(t)}. Введите ещё раз {i + 1} строку:",
                    file=erroutput)
                t = list(map(float, input.readline().strip().split()))
            matrix.append(t)
        return MyMatrix(matrix)

    def __init__(self, matrix: list[list[float]]):
        m = max([len(matrix[i]) for i in range(len(matrix))])
        n = min([len(matrix[i]) for i in range(len(matrix))])
        if m != n:
            raise MyMatrix.SizeMatrixException("Matrix was broken((:")
        self.str_count = len(matrix)
        self.column_count = len(matrix[0])
        self.matrix = matrix

    def __add__(self, other):
        if self.size() != other.size():
            raise MyMatrix.SizeMatrixException("Size of matrix must be equals!")
        return MyMatrix([[
            self[i][j] + other[i][j] for j in range(self.column_count)
        ] for i in range(self.str_count)])

    def __mul__(self, other):
        if self.column_count != other.size()[1]:
            raise MyMatrix.SizeMatrixException(
                "The number of columns of the matrix of the left argument must be equal to the number of columns of the matrix of the right argument")
        ans = [([0] * self.column_count) for _ in range(self.str_count)]
        for i in range(self.str_count):
            for j in range(self.column_count):

                for k in range(self.column_count):
                    ans[i][j] += self[i][k] * other[k][j]
        return MyMatrix(ans)

    def mul(self, other: float):
        return MyMatrix([[
            self.matrix[i][j] * other
            for j in range(self.column_count)] for i in range(self.str_count)])

    def size(self) -> tuple[int, int]:
        return self.str_count, self.column_count

    # вычисляет определитель матрицы
    def det(self) -> float:
        if self.column_count != self.str_count:
            raise MyMatrix.SizeMatrixException("The matrix must be square")
        if self.column_count == 1:
            return self[0][0]
        return sum([
            self.matrix[0][i] * self.algebraic_addition(1, i + 1)
            for i in range(self.column_count)])

    def algebraic_addition(self, i: int, j: int) -> float:  # нумерация координат с 1
        return ((-1) ** (i + j)) * self.minor(i, j)

    def minor(self, i: int, j: int) -> float:
        i, j = i - 1, j - 1  # смещение от человеческий координат (нумерация с 0, а не 1)
        ans = [self.matrix[i].copy() for i in range(self.str_count)]
        ans.pop(i)
        for k in range(len(ans)):
            ans[k].pop(j)
        return MyMatrix(ans).det()

    def transpose(self):
        return MyMatrix([
            [self.matrix[i][j] for i in range(self.str_count)]
            for j in range(self.column_count)
        ])

    def adjugate_matrix(self):
        return MyMatrix([[
            self.algebraic_addition(i + 1, j + 1)
            for j in range(self.column_count)] for i in range(self.str_count)]).transpose()

    #обратная матрица
    def inv(self):
        det = self.det()
        if det == 0:
            raise ArithmeticError("Determinant can't be zero")
        return self.adjugate_matrix().mul(1 / det)

    def __getitem__(self, item):
        return self.matrix[item]

    def __str__(self):
        str = ""
        for i in range(self.str_count):
            str += self.matrix[i].__str__()[1:-1].replace(", ", "\t") + "\n"
        return str

    class InvalidArgument(Exception):
        pass

    class SizeMatrixException(InvalidArgument):
        pass


if __name__ == '__main__':
    m = MyMatrix([[1, 0], [0, 1]])
    print(m.det())
