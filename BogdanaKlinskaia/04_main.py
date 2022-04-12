from BogdanaKlinskaia.SquareMatrix import SquareMatrix

if __name__ == '__main__':
    m = SquareMatrix.read_matrix(n=2)
    print("Собственные числа:",  *m.eigen_values())
    print("Собственные вектора:", *m.eigen_vectors())
