
a = list = []
tr = []

print("Введите количество строк")
dim = int(input())
print("Вводите элементы строки через пробел")

for i in range(dim):
  print("Строка:", i+1)
  a0 = str(input())
  b = a0.split(" ")
  a.append(b)
  for i in range(dim):
    b[i] = float(b[i])

for i in range(len(a)):
  for j in range(len(a)):
    tr.append(a[i][j])
matr = []
f = []
for i in range(len(tr)):
  f.append(float(tr[i]))
  if len(f) == len(a):
    matr.append(f)
    f = []

def sopr(a):
  c = "Самосопряженная"
  for i in range(len(a)):
    for j in range(len(a)):
      if a[i][j] != a[j][i]:
        c = "Несамосопряженная"
        break
  return c
sopra = sopr(a)

obr = list = []
st = list = []
for j in range(len(a)):
  st.append(1)
for j in range(len(a)):
  obr.append(st)

# print(obr)

def det(a):
  fact = 1
  for i in range(len(a[0])+1):
    if i > 0:
      fact = fact*i
  # подсчитал факториал
  inv = list = []
  while len(inv) != fact:
    c = ""
    while len(c) != len(a[0]):
      j = str(random.randint(1, len(a[0])))
      if str(str(j) in c) == "False":
        c = c + j
    if str(c in inv) == "False":
      inv.append(c)
  # сделал все инверсии 
  # print(inv)

  def q(i):
    b = inv[i]
    c = 0
    j = 0 
    for j in range(len(b)-1):
      k = j + 1
      while k <= len(b)-1:
        if b[j] > b[k]:
          c += 1
        k += 1
    return c 
  # подсчет перестановок
  s = 1
  d = 0
  while len(inv) != 0:
    for k in range(len(a[0])):
      s = s*a[int(inv[0][k])-1][k]
    d = d + s*((-1)**(q(0)))
    s = 1
    del(inv[0])
  return d
# minor это минор (по факту)
# минор i j 
n = len(a[0])-1
def minor(i, j):
  matr = list = []
  h = list = []
  for k in range(len(a)):
    for l in range(len(a)):
      if k != i and l != j:
        h.append(a[k][l])
  g = 0
  # print(h)
  # print(h[len(h)])
  c = list = []
  for l in range(len(a)-1):
    while len(c) != len(a)-1:
      c.append(h[g])
      g += 1
    matr.append(c)
    c = list = []
  return matr  
# print(det(a))
obra = list = []
for i in range(len(obr)):
  for j in range(len(obr)):
    # print(minor(i, j))
    s = minor(i, j)
    # print(det(s))
    obr[i][j] = ((-1)**(i+j))*det(s)
    obra.append(obr[i][j])

obrat = list = []
g = 0
c = list = []
for l in range(len(a)):
    while len(c) != len(a):
      c.append(obra[g])
      g += 1
    obrat.append(c)
    c = list = [] 
obratn = list = [] #обратная матрица
b = list = []
if det(a) != 0:
  for i in range(len(a)):
    for j in range(len(a)):
      b.append((obrat[j][i])/(det(a)))
      # b.append(obrat[j][i])
    obratn.append(b)
    b = list = []

def uni(matr, obratn, a):
  c = ""
  if det(a) != 0:
    с = ""
    for i in range(len(a)):
      for j in range(len(a)):
        if matr[j][i] != obratn[i][j]:
          c = "Неунитарная"
    if c == "":
      c = "Унитарная"
  else:
    c = "Неунитарная"
  return c

print("Матрица:")
print(uni(matr, obratn, a))
print(sopra)
