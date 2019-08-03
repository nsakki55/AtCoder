#include <iostream>
using namespace std;


int main(){
    int n_ball,n_person;
    cin>>n_ball>>n_person;
    if(n_person==1){
        cout<<0<<endl;
    }
    else{
        int max_num=n_ball-n_person;
        cout<<max_num<<endl;
    }
    return 0;
}