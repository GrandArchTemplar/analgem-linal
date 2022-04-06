import sys

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


if __name__ == '__main__':
    m = SquareMatrix.read_matrix(n=3)
    print(m)
