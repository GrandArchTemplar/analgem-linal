import math

row = 2
col = 2
print("Введите элементы матрицы 2 х 2 по одному(движемся слева направо, сверху вниз): ")
final_matrix = []
for i in range(row):
    sub_matrix = []
    for j in range(col):
        sub_matrix.append(float(input()))
    final_matrix.append(sub_matrix)
print('Ваша матрица:) Убедитесь, пожалуйста, что все правильно ввели: ', final_matrix)

d = (final_matrix[0][0] + final_matrix[1][1])**2 - 4*(final_matrix[0][0]*final_matrix[1][1] - final_matrix[1][0]*final_matrix[0][1])
l1 = round((final_matrix[0][0] + final_matrix[1][1] + math.sqrt(d))/2, 4)
l2 = round((final_matrix[0][0] + final_matrix[1][1] - math.sqrt(d))/2, 4)

print('Внимание! Представляем вам собственные значения!')
print("Значение раз: ", l1)
print("Значение два: ", l2)

if final_matrix[0][0] - l1 != 0 and final_matrix[0][1] != 0:
    x = 1
    y = round(-(final_matrix[0][0] - l1)/final_matrix[0][1], 4)
elif final_matrix[1][1] - l1 != 0:
    x = 1
    y = round(-final_matrix[1][0]/(final_matrix[1][1] - l1), 4)
elif final_matrix[0][0] - l2 != 0 and final_matrix[0][1] != 0:
    x = 1
    y = round(-(final_matrix[0][0] - l2)/final_matrix[0][1], 4)
elif final_matrix[1][1] - l2 != 0:
    x = 1
    y = round(-final_matrix[1][0]/(final_matrix[1][1] - l2), 4)
else:
    x = 0
    y = 1


print('Координаты нашего собственного вектора: x = ', x, ', y = ', y)