#include <iostream>
#include <string>
#include <cmath>

using namespace std;

pair<float, float> roots2(float a, float b, float c) //êîðíè êâàäðàòíîãî òðåõ÷ëåíà
{
    float d = b*b-4*a*c;
    if (d<0)
        return pair<float, float> (666, 666);
    else if (abs(d)<0.000000001)
        return pair<float, float> (-b/2/a, -b/2/a);
    else
        return pair<float, float> ((-b-sqrt(d))/2/a, (-b+sqrt(d))/2/a);
}

pair<float, float> sys(float a, float b, float c, float d) //ñèñòåìà óðàâíåíèé
{
    float x, y;
    if(abs(b)<0.000001 && abs(c)<0.000001)
    {
        if(abs(a)<0.000001 && abs(d)<0.000001)
        {
            x = 666.6;
            y = 666.6;
        }
        else if(abs(a)<0.000001)
        {
            x = 666.6;
            y = 0;
        }
        else if(abs(d)<0.000001)
        {
            x = 0;
            y = 666.6;
        }
    }
    else if(abs(b)<0.0000001)
    {
        if(abs(a)<0.000001 && abs(d)<0.000001)
        {
            x = 0;
            y = 666.6;
        }
        else if(abs(a)<0.000001)
        {
            x = 1;
            y = c/d;
        }
        else if(abs(d)<0.000001)
        {
            x = 0;
            y = 666.6;
        }
        else
        {
            x = 0;
            y = 0;
        }
    }
    else if(abs(c)<0.0000001)
    {
        if(abs(d)<0.000001 && abs(a)<0.000001)
        {
            y = 0;
            x = 666.6;
        }
        else if(abs(d)<0.000001)
        {
            y = 1;
            x = b/a;
        }
        else if(abs(a)<0.000001)
        {
            y = 0;
            x = 666.6;
        }
        else
        {
            y = 0;
            x = 0;
        }
    }
    else if(abs(a)>0.0000001 && abs(b)>0.0000001 && abs(c)>0.0000001 && abs(d)>0.0000001)
    {
        if(abs(a/c-b/d)<0.000001)
        {
            if(abs(a-b)<0.000001)
            {
                x = 1;
                y = 1;
            }
            else
            {
                x = 1;
                y =a/b;
            }
        }
    }
    return pair<float, float> (x, y);
}

struct Matrix
{
    int length;
    int height;
    float **body;

    void CreateBody(int h, int l)
    {
        height = h;
        length = l;
        body = new float* [height];
        for(int i=0; i<height; i++)
            body[i] = new float[length];
    }

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

    void SetBodyForSP(pair <float, float> v1, pair <float, float> v2) //îòäåëüíûé ââîä äëÿ ïîèñêà ïðîåêòîðîâ
    {
        height = 2;
        length = 2;
        body = new float* [height];
        for(int i=0; i<height; i++)
        {
         body[i] = new float[length];
        }
        body[0][0] = v1.first;
        body[0][1] = v2.first;
        body[1][0] = v1.second;
        body[1][1] = v2.second;
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
            cout<<"ERROR (sum)";
            exit(0);
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
            cout<<"ERROR (mult)";
            exit(1);
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

    bool operator==(Matrix m2)
    {
        if(height != m2.height || length != m2.length)
            return false;
        for(int i=0; i<height; i++)
        {
            for(int j=0; j<length; j++)
            {
                if(body[i][j] != m2.body[i][j])
                    return false;
            }
        }
        return true;
    }

    static float Det(Matrix m) //îïðåäåëèòåëü
    {
        if(m.height != m.length)
        {
            cout<<"ERROR (Det)";
            exit(2);
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

    static Matrix Trans(Matrix m) //òðàíñïîíèðîâàííàÿ
    {
        Matrix ans = Matrix();
        ans.height = m.length;
        ans.length = m.height;

        ans.body = new float* [ans.height];
        for(int i=0; i<ans.height; i++)
        {
         ans.body[i] = new float[ans.length];
            for(int j=0; j<ans.length; j++)
            {
                ans.body[i][j] = m.body[j][i];
            }
        }

        return ans;
    }

    static Matrix Uni(Matrix m) //ñîþçíàÿ
    {
        if(m.height != m.length)
        {
            cout<<"ERROR (Uni)";
            exit(3);
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
            cout<<"ERROR (Uni)";
            exit(4);
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

    static Matrix Rev(Matrix m) //îáðàòíàÿ
    {
        return Trans(Uni(m));
    }

    static void HP(Matrix m) //õàðàêòåðèñòè÷åñêèé ïîëèíîì
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

    static void SV(Matrix m) //ñîáñòâåííûå âåêòîðà
    {
        float a0 = m.body[0][0];
        float b0 = m.body[0][1];
        float c0 = m.body[1][0];
        float d0 = m.body[1][1];

        pair<float, float> roots = roots2(1, -a0-d0, a0*d0-b0*c0);
        if(roots.first == roots.second)
        {
            if(roots.first == 666)
            {
                cout<<"There are no sobstvennye vectors";
                exit(5);
            }
            pair<float, float> ans = sys(a0-roots.first, -b0, c0, roots.first-d0);
            cout<<roots.first<<" ("<<ans.first<<", "<<ans.second<<")";
        }
        else
        {
            pair<float, float> ans1 = sys(a0-roots.first, -b0, c0, roots.first-d0);
            pair<float, float> ans2 = sys(a0-roots.second, -b0, c0, roots.second-d0);
            cout<<roots.first<<" ("<<ans1.first<<", "<<ans1.second<<")"<<endl<<roots.second<<" ("<<ans2.first<<", "<<ans2.second<<")";
        }
    }

    static void SP(Matrix m) //ñîáñòâåííûå ïðîåêòîðû
    {
        float a0 = m.body[0][0];
        float b0 = m.body[0][1];
        float c0 = m.body[1][0];
        float d0 = m.body[1][1];

        pair<float, float> roots = roots2(1, -a0-d0, a0*d0-b0*c0);
        if(roots.first == roots.second)
        {
            cout<<"There are no adekvatnye sobstvennye proectors";
            exit(6);
        }
        else
        {
            pair<float, float> v1 = sys(a0-roots.first, -b0, c0, roots.first-d0);
            pair<float, float> v2 = sys(a0-roots.second, -b0, c0, roots.second-d0);

            Matrix mm = Matrix();
            Matrix m1 = Matrix();
            Matrix m2 = Matrix();
            Matrix m1t = Matrix();
            Matrix m2t = Matrix();

            mm.SetBodyForSP(v1, v2);

            m1.CreateBody(2, 1);
            m2.CreateBody(2, 1);
            m1t.CreateBody(1, 2);
            m2t.CreateBody(1, 2);

            m1.body[0][0] = mm.body[0][0];
            m1.body[1][0] = mm.body[1][0];
            m1t.body[0][0] = Matrix::Rev(mm).body[0][0];
            m1t.body[0][1] = Matrix::Rev(mm).body[0][1];
            cout<<roots.first<<":"<<endl;
            (m1*m1t).GetBody();

            m2.body[0][0] = mm.body[0][1];
            m2.body[1][0] = mm.body[1][1];
            m2t.body[0][0] = Matrix::Rev(mm).body[1][0];
            m2t.body[0][1] = Matrix::Rev(mm).body[1][1];
            cout<<roots.second<<":"<<endl;
            (m2*m2t).GetBody();
        }
    }

    static void US(Matrix m) //óíèòàðíîñòü è ñàìîñîïðÿæåííîñòü
    {
        if(Det(m) != 0 && Trans(m)==Rev(m))
            cout<<"unitarnaya"<<endl;
        else
            cout<<"NEunitarnaya"<<endl;
        if(Trans(m)==m)
            cout<<"samosopryajonnaya"<<endl;
        else
            cout<<"NEsamosopryajonnaya"<<endl;
    }

    static int Trace(Matrix m) //ñêàëÿðíîå ïðîèçâåäåíèå
    {
        if(m.height != m.length)
        {
            cout<<"ERROR (Trace)";
            exit(7);
        }
        int s = 0;
        for(int i=0; i<m.height; i++)
        {
            s+=m.body[i][i];
        }
        return s;
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
    while(x != 1 && x != 2 && x != 3 && x != 4 && x != 5 && x != 6 && x != 7 && x != 8)
    {
        if(x == -1000) cout<<"Choose option: 1-sum 2-mult (multiki pokazhet (net)) 3-reverse 4-polynyam 5-Victori 6-spector-prorector 7-unitarnost':";
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
        if(x == 5)
        {
            Matrix m = Matrix();
            m.SetBody(2, 2);
            cout<<endl;
            Matrix::SV(m);
        }
        if(x == 6)
        {
            Matrix m = Matrix();
            m.SetBody(2, 2);
            cout<<endl;
            Matrix::SP(m);
        }
        if(x == 7)
        {
            Matrix m = Matrix();
            m.SetBody();
            cout<<endl;
            Matrix::US(m);
        }
    }
}
