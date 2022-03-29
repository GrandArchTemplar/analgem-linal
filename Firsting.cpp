#include <iostream>

using namespace std;

struct Matrix
{
    int length;
    int height;
    float **body;

    void SetBody()
    {
        cout<<"Lines count:";
        cin>>height;
        cout<<"Columns count:";
        cin>>length;
        body = new float* [height];
        for(int i=0; i<height; i++)
        {
         body[i] = new float[length];
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

    Matrix operator+(Matrix m2)
    {
        if(height != m2.height || length != m2.length)
        {
            cout<<"ERROR";
            throw exception();
        }
        Matrix ans = Matrix();
        ans.height = height;
        ans.length = length;
        ans.body = new float* [ans.height];
        for(int i=0; i<ans.height; i++)
        {
            ans.body[i] = new float[ans.length];
            for(int j=0; j<ans.length; j++)
            {
                ans.body[i][j] = body[i][j] + m2.body[i][j];
            }
        }
        return ans;
    }

    Matrix operator*(Matrix m2)
    {
        if(length != m2.height)
        {
            cout<<"ERROR";
            throw exception();
        }
        Matrix ans = Matrix();
        ans.length = m2.length;
        ans.height = height;
        ans.body = new float* [ans.height];
        for(int i=0; i<ans.height; i++)
        {
            ans.body[i] = new float[ans.length];
            for(int j=0; j<m2.length; j++)
            {
                for(int k=0; k<length; k++)
                {
                    ans.body[i][j] += body[i][k]*m2.body[k][j];
                }
            }
        }
        return ans;
    }

    static float Det(Matrix m)
    {
        if(m.height != m.length)
        {
            cout<<"ERROR";
            throw exception();
        }
        if(m.height != 1)
        {
            Matrix nm = Matrix();
            nm.height = m.height-1;
            nm.length = nm.height;

            int xx = 1;
            float ans = 0;
            for(int x=0; x<m.length; x++)
            {
                int ik = 0;
                nm.body = new float*[nm.height];
                for(int i=1; i<m.height; i++)
                {
                    int jk = 0;
                    nm.body[ik] = new float[nm.length];
                    for(int j=0; j<m.length; j++)
                    {
                        if(j == x) continue;
                        nm.body[ik][jk] = m.body[i][j];
                        jk++;
                    }
                    ik++;
                }
                ans += xx*m.body[0][x]*Det(nm);
                xx = -xx;
                for(int i=0; i<nm.height; i++)
                {
                    delete[] nm.body[i];
                }
                delete[] nm.body;
            }
            return ans;
        }
        else
        {
            return m.body[0][0];
        }
    }

    static Matrix Trans(Matrix m)
    {
        if(m.height != m.length)
        {
            cout<<"ERROR";
            throw exception();
        }
        for(int i=0; i<m.height; i++)
        {
            for(int j=i; j<m.length; j++)
            {
                float d = m.body[i][j];
                m.body[i][j] = m.body[j][i];
                m.body[j][i] = d;
            }
        }
        return m;
    }

    static Matrix Uni(Matrix m)
    {
        if(m.height != m.length)
        {
            cout<<"ERROR";
            throw exception();
        }
        if(m.height == 1)
        {
            Matrix ans = Matrix();
            ans.height = 1;
            ans.length = 1;
            ans.body = new float*[ans.height];
            ans.body[0] = new float[ans.length];
            ans.body[0][0] = 1/m.body[0][0];
            return ans;
        }

        Matrix nm = Matrix();
        nm.height = m.height-1;
        nm.length = nm.height;

        Matrix ans = Matrix();
        ans.height = m.height;
        ans.length = m.length;

        ans.body = new float*[ans.height];
        for(int i=0; i<ans.height; i++)
        {
            ans.body[i] = new float[ans.length];
            for(int j=0; j<ans.length; j++)
            {
                ans.body[i][j]=0;
            }
        }

        int xx = 1;
        float d = Det(m);
        if (d == 0)
        {
            cout<<"ERROR";
            throw exception();
        }

        for(int y=0; y<m.height; y++)
        {
            for(int x=0; x<m.length; x++)
            {
                int ik = 0;
                nm.body = new float*[nm.height];
                for(int i=0; i<m.height; i++)
                {
                    if(i == y) continue;
                    else
                    {
                        int jk = 0;
                        nm.body[ik] = new float[nm.length];
                        for(int j=0; j<m.length; j++)
                        {
                            if(j == x) continue;
                            nm.body[ik][jk] = m.body[i][j];
                            jk++;
                        }
                        ik++;
                    }
                }
                ans.body[y][x] = xx*Det(nm)/d;
                xx = -xx;
                for(int i=0; i<nm.height; i++)
                {
                    delete[] nm.body[i];
                }
                delete[] nm.body;
            }
            xx = -xx;
        }
        return ans;
    }

    static Matrix Rev(Matrix m)
    {
        return Trans(Uni(m));
    }

    ~Matrix()
    {
        for(int i=0; i<height; i++)
        {
            delete[] body[i];
        }
        delete[] body;
        height = 0;
        length = 0;
    }

};


int main()
{
    int x = -1000;
    while(x != 1 && x != 2 && x != 3)
    {
        if(x == -1000) cout<<"Choose option: 1-sum 2-mult (multiki pokazhet (net)) 3-reverse:";
        else cout<<"escsche raz";
        cin>>x;
        if(x == 1)
        {
            Matrix m1 = Matrix();
            Matrix m2 = Matrix();
            m1.SetBody();
            cout<<endl;
            m2.SetBody();
            cout<<endl;
            (m1+m2).GetBody();
        }
        if(x == 2)
        {
            Matrix m1 = Matrix();
            Matrix m2 = Matrix();
            m1.SetBody();
            cout<<endl;
            m2.SetBody();
            cout<<endl;
            (m1*m2).GetBody();
        }
        if(x == 3)
        {
            Matrix m = Matrix();
            m.SetBody();
            cout<<endl;
            Matrix::Rev(m).GetBody();
        }
    }
}
