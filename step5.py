A = []
print("Введите данные по строкам слева направо:")
for i in range(2):
    a = []
    for j in range(2):
        a.append(int(input()))
    A.append(a)
pipa=0
a1=A[0][0]
b1=A[0][1]
c1=A[1][0]
d1=A[1][1]
a=1
b=(a1+d1)*(-1)
c=a1*d1-b1*c1
l1=((-1)*b+((b*b-4*a*c)**0.5))/2
l2=((-1)*b-((b*b-4*a*c)**0.5))/2
Vector1=[0]
Vector2=[0]
Vector3=[0]
try:
    try:
        x1=1
        x2=c1*x1/(l1-d1)
        print('число:',l1, 'вектор: [',x1,",", x2,"]")
        Vector1=[x1,x2]
    except:
        x2=1
        x1=b1*x2/(l1-a1)
        print('число:', l1, 'вектор: [',x1,",", x2,"]")
        Vector1 = [x1, x2]
    try:
        x1=1
        x2=c1*x1/(l2-d1)
        print('число:',l2, 'вектор: [',x1,",", x2,"]")
        Vector2 = [x1, x2]
    except:
        x2=1
        x1=b1*x2/(l2-a1)
        print('число:', l2, 'вектор: [',x1,",", x2,"]")
        Vector2 = [x1, x2]
except:
    print('число:', 0, 'вектор: [',1,",", 0,"]")
    pipa=1
    print("error")
if pipa!=1:
    print('')
    PASHA=[[Vector1[0],Vector2[0]],[Vector1[1],Vector2[1]]]
    DET=PASHA[0][0]*PASHA[1][1]-PASHA[1][0]*PASHA[0][1]
    M=[[PASHA[1][1],-PASHA[0][1]],[-PASHA[1][0],PASHA[0][0]]]
    k1=PASHA[1][1]/DET
    k2=(-1)*PASHA[0][1]/DET
    k3=(-1)*PASHA[1][0]/DET
    k4=PASHA[0][0]/DET
    S=[[k1,k2],[k3,k4]]
    P1 = [[PASHA[0][0]*S[0][0],PASHA[0][0]*S[0][1]],[PASHA[1][0]*S[0][0],PASHA[1][0]*S[0][1]]]
    P2 = [[PASHA[0][1]*S[1][0],PASHA[0][1]*S[1][1]],[PASHA[1][1]*S[1][0],PASHA[1][1]*S[1][1]]]
    print("проектор 1:")
    for i in range(2):
        for j in range(2):
            print(P1[i][j], end=" ")
        print()
    print(" ")
    print("проектор 2:")
    print("")
    for i in range(2):
        for j in range(2):
            print(P2[i][j], end=" ")
        print()

