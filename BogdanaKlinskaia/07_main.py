if __name__ == '__main__':
    n = int(input())
    mat = [list(map(float, input().split())) for i in range(n)]
    for d in range(1, n):
        c = [0] * n


        def proectsiya(d, j):
            nr = 0
            sp = 0
            for i in range(n):
                b = mat[d - j - 1]
                a = mat[d]
                sp += b[i] * a[i]
                nr += b[i] * b[i]
            l = sp / nr
            return l


        for i in range(n):
            for j in range(d):
                c[i] += mat[d - j - 1][i] * proectsiya(d, j)
        for i in range(n):
            mat[d][i] = mat[d][i] - c[i]
    for i in range(n):
        print(*mat[i])
