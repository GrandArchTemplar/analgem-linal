row = int(input("Введите количество строк матрицы: "))
col = int(input("Введите количество столбцов матрицы: "))
print("Введите элементы по одному(движемся слева направо, сверху вниз): ")
final_matrix = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(int(input()))
    final_matrix.append(sub_matrix)
print('Ваша матрица:) Убедитесь, пожалуйста, что все правильно ввели: ', final_matrix)

b = final_matrix[0][0] + final_matrix[1][1] + final_matrix[2][2]
c = final_matrix[0][0] * final_matrix[1][1] + final_matrix[0][0] * final_matrix[2][2] + final_matrix[2][0] * final_matrix[0][2] + final_matrix[2][1] * final_matrix[1][2] + final_matrix[1][0] * final_matrix[0][1]
d = final_matrix[0][0] * final_matrix[1][1] * final_matrix[2][2] + final_matrix[1][0] * final_matrix[2][1] * final_matrix[0][2] + final_matrix[0][1] * final_matrix[1][2] * final_matrix[2][0] - final_matrix[2][0] * final_matrix[0][2] * final_matrix[1][1] - final_matrix[0][0] * final_matrix[2][1] * final_matrix[1][2] - final_matrix[1][0] * final_matrix[0][1] * final_matrix[2][2]

if b >= 0 and c >= 0 and d >= 0:
    print('-xxx +', b,'xx +', c, 'x +', d)
elif b >= 0 and c >= 0 and d < 0:
    print('-xxx', '+', b, 'xx', '+', c, 'x', d)
elif b >= 0 and c < 0 and d > 0:
    print('-xxx', '+', b,'xx', c, 'x', '+', d)
elif b < 0 and c >= 0 and d >= 0:
    print('-xxx', b, 'xx', '+', c, 'x', '+', d)
elif b < 0 and c < 0 and d >= 0:
    print('-xxx', b, 'xx', c, 'x', '+', d)
elif b < 0 and c >= 0 and d < 0:
    print('-xxx', b, 'xx', '+', c, 'x', d)
elif b >= 0 and c < 0 and d < 0:
    print('-xxx', '+', b, 'xx', c, 'x', d)
else:
    print('-xxx', b, 'xx', c, 'x', d)