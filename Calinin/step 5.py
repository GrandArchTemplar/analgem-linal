# Ввод матрицы
m = []
print("Вводите строки матрицы (enter после каждой строки). Элементы в строке разделяйте пробелами")
for i in range(2):
    b = list(input().split())
    m.append(b)
for i in range(2):
    for j in range(2):
        m[i][j] = float(m[i][j])
D = (m[0][0] + m[1][1])**2 - 4*(m[0][0]*m[1][1] - m[0][1]*m[1][0])
# собственные значения
L1 = (m[0][0] + m[1][1] - D ** 0.5)/2
L2 = (m[0][0] + m[1][1] + D ** 0.5)/2
# собственные векторы
vectorL1 = [0, 0]
vectorL2 = [0, 0]
#  вектор 1
if m[0][1] == 0 and (m[0][0] - L1) == 0 and m[1][0] == 0 and (m[1][1] - L1) == 0:
    vectorL1 = [1, 1]
elif (m[0][0] - L1) == 0 and m[1][0] == 0:
    vectorL1 = [1, 0]
elif m[0][1] == 0 and (m[1][1] - L1) == 0:
    vectorL1 = [0, 1]
elif m[0][1] == 0:
    vectorL1 = [(m[1][1] - L1), -m[1][0]]
else:
    vectorL1 = [m[0][1], (L1 - m[0][0])]
# вектор 2
if m[0][1] == 0 and (m[0][0] - L2) == 0 and m[1][0] == 0 and (m[1][1] - L2) == 0:
    vectorL2 = [1, 1]
elif (m[0][0] - L2) == 0 and m[1][0] == 0:
    vectorL2 = [1, 0]
elif m[0][1] == 0 and (m[1][1] - L2) == 0:
    vectorL2 = [0, 1]
elif m[0][1] == 0:
    vectorL2 = [(m[1][1] - L2), -m[1][0]]
else:
    vectorL2 = [m[0][1], (L2 - m[0][0])]

T = [[vectorL1[0], vectorL2[0]], [vectorL1[1], vectorL2[1]]]

det = T[0][0]*T[1][1] - T[0][1]*T[1][0]

S = [[T[1][1]/det, T[0][1]/det], [T[1][0]/det, T[0][0]/det]]

Pr1 = [[T[0][0]*S[0][0], T[0][0]*S[0][1]], [T[1][0]*S[0][0], T[1][0]*S[0][1]]]
Pr2 = [[T[0][1]*S[1][0], T[0][1]*S[1][1]], [T[1][1]*S[1][0], T[1][1]*S[1][1]]]

print ('Проектор 1')
for i in Pr1:
    print (i)
print ('Проектор 2')
for i in Pr2:
    print (i)