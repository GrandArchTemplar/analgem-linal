from SquareMatrix import SquareMatrix

if __name__ == '__main__':
    matrix = SquareMatrix.read_matrix(n=3)
    print(matrix.char_polynom())
