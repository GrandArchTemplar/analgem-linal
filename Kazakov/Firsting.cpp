#include <iostream>

using namespace std;

class Matrix
{
public:
    int length = 0;
    int height = 0;
    int **body;

    void SetBody()
    {
        cout<<"Lines count:";
        cin>>height;
        cout<<"Columns count:";
        cin>>length;
        body = new int* [height];
        for(int i=0; i<height; i++)
        {
         body[i] = new int[length];
            for(int j=0; j<length; j++)
            {
                cin>>body[i][j];
            }
        }
    }

    void GetBody()
    {
        for(int i=0; i<height; i++)
        {
            for(int j=0; j<length; j++)
            {
                cout<<body[i][j]<<" ";
            }
            cout<<endl;
        }
    }

    ~Matrix()
    {
        for(int i=0; i<height; i++)
        {
            delete[] body[i];
        }
        delete[] body;
    }
};

Matrix sum(Matrix m1, Matrix m2)
{
    if(m1.height != m2.height || m1.length != m2.length)
    {
        cout<<"ERROR";
        exit;
    }
    Matrix ans = Matrix();
    ans.height = m1.height;
    ans.length = m1.length;
    ans.body = new int* [ans.height];
    for(int i=0; i<ans.height; i++)
    { 
        ans.body[i] = new int[ans.length];
        for(int j=0; j<ans.length; j++)
        {
            ans.body[i][j] = m1.body[i][j] + m2.body[i][j];
        }
    }
    return ans;
}

Matrix mult(Matrix m1, Matrix m2)
{
    if(m1.length != m2.height)
    {
        cout<<"ERROR";
        exit;
    }
    Matrix ans = Matrix();
    ans.length = m2.length;
    ans.height = m1.height;
    ans.body = new int* [ans.height];
    for(int i=0; i<ans.height; i++)
    {
        ans.body[i] = new int[ans.length];
        for(int j=0; j<m2.length; j++)
        {
            for(int k=0; k<m1.length; k++)
            {
                ans.body[i][j] += m1.body[i][k]*m2.body[k][j];
            }
        }
    }
    return ans;
}

int main()
{
    Matrix m1 = Matrix();
    Matrix m2 = Matrix();

    m1.SetBody();
    m2.SetBody();

    int x = -1000;
    while(x != 1 && x != 2)
    {
        if(x == -1000) cout<<"Choose option: 1-sum 2-mult (multiki pokazhet (net))";
        else cout<<"escsche raz";
        cin>>x;
        if(x == 1) sum(m1, m2).GetBody();
        if(x == 2) mult(m1, m2).GetBody();
    }
}
