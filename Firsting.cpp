#include <iostream>
#include <string>

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

    void SetBody(int m, int n)
    {
        height = m;
        length = n;
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
                if(x%2==0) xx = 1;
                else xx = -1;
                ans += xx*m.body[0][x]*Det(nm);
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
                if((x+y)%2==0) xx = 1;
                else xx = -1;
                ans.body[y][x] = xx*Det(nm)/d;
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

    static void HP(Matrix m)
    {
        float d[9];
        for(int i=0; i<9; i++)
            d[i] = m.body[i/3][i%3];
        int coefs[4];
        coefs[0] = Det(m);
        coefs[1] = d[5]*d[7]+d[1]*d[3]+d[2]*d[6]-d[0]*d[4]-d[0]*d[8]-d[4]*d[8];
        coefs[2] = d[0]+d[4]+d[8];
        coefs[3] = -1;
        string s = "-xxx";

        if(coefs[2]>0) s += "+" + to_string(coefs[2]) + "xx";
        else if(coefs[2]<0) s += to_string(coefs[2]) + "xx";
        if(coefs[1]>0) s += "+" + to_string(coefs[1]) + "x";
        else if(coefs[1]<0) s += to_string(coefs[1]) + "x";
        if(coefs[0]>0) s += "+" + to_string(coefs[0]);
        else if(coefs[0]<0) s += to_string(coefs[0]);
        cout<<s;
        return;
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
    while(x != 1 && x != 2 && x != 3 && x != 4)
    {
        if(x == -1000) cout<<"Choose option: 1-sum 2-mult (multiki pokazhet (net)) 3-reverse 4-polynyam:";
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
        if(x == 4)
        {
            Matrix m = Matrix();
            m.SetBody(3, 3);
            cout<<endl;
            Matrix::HP(m);
        }
    }
}
