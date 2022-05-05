import sys
from math import sqrt

from MyMatrix import MyMatrix
from MyPolinom import MyPolinom


class SquareMatrix(MyMatrix):
    @staticmethod
    def read_matrix(n: int = None, input=sys.stdin, output=sys.stdout, erroutput=sys.stderr):
        if n is None:
            print(
                "Введите кол-во строк (целое число) в матрице, нажмите eneter, затем введите строки матрицы, разделяя столбцы пробелом, а строки enter-ом:",
                file=output)
            n = int(input.readline().strip())
        else:
            print(
                f"Введите строки матрицы {n} на {n}, разделяя столбцы пробелом, а строки enter-ом:"
            )
        matrix = []

        for i in range(n):
            t = list(map(float, input.readline().strip().split()))
            while len(t) != n:
                print(
                    f"Что-то пошло не так, должно быть {n} элементов в строке, а получлось {len(t)}. Введите ещё раз {i + 1} строку:",
                    file=erroutput)
                t = list(map(float, input.readline().strip().split()))
            matrix.append(t)
        return SquareMatrix(matrix)

    def __init__(self, matrix: list[list[float]]):
        super().__init__(matrix)
        self.n = self.str_count
        if self.column_count != self.str_count:
            raise SquareMatrix.SizeMatrixException(f"It's NOT {self.n} square matrix((::")

    def char_polynom(self) -> MyPolinom:
        assert self.n == 3, "char_polynom() написана только для матриц 3 на 3"
        a = self.matrix
        return MyPolinom([
            - a[0][2] * a[1][1] * a[2][0] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] - a[0][0] * a[1][
                2] * a[2][1] - a[0][1] * a[1][0] * a[2][2] + a[0][0] * a[1][1] * a[2][2],
            a[0][1] * a[1][0] - a[0][0] * a[1][1] + a[0][2] * a[2][0] + a[1][2] * a[2][1] - a[0][0] * a[2][2] - a[1][
                1] * a[2][2],
            a[0][0] + a[1][1] + a[2][2],
            -1,
        ])

    def eigen_values(self) -> list[float]:
        assert self.n == 2, "eigen_values() написана только для матриц 2 на 2"
        x = self.matrix
        sq = sqrt(x[0][0] ** 2 - 2 * x[1][1] * x[0][0] + x[1][1] ** 2 + 4 * x[0][1] * x[1][0])
        l1 = 0.5 * (x[0][0] + x[1][1] - sq)
        if sq == 0:
            return [l1]
        return [l1, l1 + sq]

    def eigen_vectors(self) -> list[list[float]]:
        assert self.n == 2, "eigen_vectors() написана только для матриц 2 на 2"
        if self.matrix[1][0] != 0:
            l1, l2 = self.eigen_values()
            l1 = -(l1 - self.matrix[0][0]) / self.matrix[1][0]
            l2 = -(l1 - self.matrix[0][0]) / self.matrix[1][0]
            return [[l1, 1], [l2, 1]]
        else:
            if self.matrix[0][0] != self.matrix[1][1]:
                return [[1, 0], [self[0][1] / (self[1][1] - self[0][0]), 1]]
            else:
                return [[1, 0]]

    def get_proectors(self) -> list:
        t = MyMatrix(self.eigen_vectors()).transpose()
        assert t.column_count == t.str_count, "Матрица должна быть квадратной"
        s = t.inv()
        return [MyMatrix(t.get_column(i)) * MyMatrix([s.get_row(i)]) for i in range(t.str_count)]


if __name__ == '__main__':
    m = SquareMatrix.read_matrix(n=2)
    print(m.eigen_values())
    print(m.eigen_vectors())
