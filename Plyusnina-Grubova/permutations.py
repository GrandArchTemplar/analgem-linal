from itertools import permutations


def generate(n):
    return permutations(range(n))


def parity(perm):
    cnt = 0
    for i in range(len(perm)):
        for j in range(i):
            if perm[j] > perm[i]:
                cnt += 1
    return cnt % 2
