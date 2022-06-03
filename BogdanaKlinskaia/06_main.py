from SquareMatrix import SquareMatrix, MyMatrix

if __name__ == '__main__':
    m = SquareMatrix.read_matrix()
    print(f"Симметрична: {m.isSimmetric()}")
    print(f"Унитарна: {m.isUnitar()}")
