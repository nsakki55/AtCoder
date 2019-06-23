#include<iostream>
using namespace std;

unsigned euclidean_gcd(unsigned a,unsigned b){
    while(1){
        if( a < b) swap(a,b);
        if( !b ) break;
        a%=b;
    }
    return a;
}

int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;

//c,dの倍数の個数を求める
    int Bc_cnt=b/c;
    int Bd_cnt=b/d;

    int g=euclidean_gcd(c,d);
    int l=c*d/g;
    int b_over_devide=b/l;
    int B_num=b-Bc_cnt-Bd_cnt+b_over_devide;


    int Ac_cnt=a-1/c;
    int Ad_cnt=a-1/d;
    int a_over_devide=a/l;
    int A_num=a-1 -Ac_cnt-Ad_cnt+a_over_devide;
    
    cout<<B_num-A_num<<endl;
    
    return 0;
}