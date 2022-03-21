#include <string>
#include <iostream>
#include <clocale>
#include <Windows.h>
using namespace std;
int ** create_martix(int n, int m)
{
    int **A = new int*[n];
    for(int i = 0; i<n;i++)
    {
        A[i] = new int[m];
    }
    return A;
}
void input_matrix(int **A, int n, int m){
    for (int i=0; i < n;i++){
        for (int j=0; j<m;j++){
            cout << "Введите элемент с индексом =" << i+1 << j+1 << endl;
            cin >> A[i][j];
        }
    }
}
void output_matrix(int **A, int n, int m){
    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}
void output_matrix_componly(int**A,int n, int y){
    for(int i=0;i<n;i++){
        for(int j=0;j<y;j++){
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}
void sum_matrix(int **A,int **B, int **Res, int n, int m){
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<m;j++)
        {
            Res[i][j] += A[i][j] + B[i][j];
        }
    }
}
void comp_matrix(int **A,int **B,int **Res, int n, int m, int x, int y){
    for (int i=0;i<n;i++)
    {
        for (int j=0;j<y;j++)
        {
            for(int k=0;k<m;k++)
                Res[i][j] += A[i][k] * B[k][j];
        }
    }
}
int main() {
    SetConsoleOutputCP(866);
    setlocale(LC_ALL, "RUS");
    int n, m, x, y;
    cout << "Кол-во строк/столбцов первой матрицы" << endl;
    cin >> n >> m;
    cout << "Кол-во строк/столбцов второй матрицы" << endl;
    cin >> x >> y;
    int **T = create_martix(n, m);
    int **S = create_martix(x, y);
    int **C = create_martix(n, m);
    int **M = create_martix(n, m);
    input_matrix(T, n, m);
    input_matrix(S, x, y);
    if ((n == x) and (m == y) and (m == x)) {
        sum_matrix(T, S, C, n, m);
        comp_matrix(T, S, M, n, m, x, y);
        cout << "Сумма матриц" << endl;
        output_matrix(C, n, m);
        cout << "Умножение матриц" << endl;
        output_matrix(M, n, m);
        return 0;
    }
    else if ((n == x) and (m == y) and (m != x)) {
        sum_matrix(T, S, C, n, m);
        cout << "Сумма матриц" << endl;
        output_matrix(C, n, m);
        cout << "Умножение матриц невозможно" << endl;
        return 0;
    }
    else if (((n != x) or (m != y)) and (m == x)) {
        comp_matrix(T, S, M, n, m, x, y);
        cout << "Сумма матриц невозможна" << endl;
        cout << "Умножение матриц" << endl;
        output_matrix_componly(M, n, y);
        return 0;
    }
    else {
        cout << "И сумма, и умножение невозможно";}
}
