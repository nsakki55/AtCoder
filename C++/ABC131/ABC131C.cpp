#include<iostream>
using namespace std;

int main(){
    int a,b,c,d;
    cin>>a>>b>>c>>d;

    int count=0;
    for(int i=a;i<=b;i++){
        if(i%c!=0 && i%d!=0) count++;
    }
    cout<<count<<endl;
    return 0;
}