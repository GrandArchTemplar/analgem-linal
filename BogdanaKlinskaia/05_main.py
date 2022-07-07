from SquareMatrix import SquareMatrix

if __name__ == '__main__':
    m = SquareMatrix.read_matrix(n=2)
    print("Cобственные проекторы:", *m.get_proectors(), sep='\n')
