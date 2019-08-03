#include <bits/stdc++.h>
using namespace std;


 int main(){
     int a,b;
     cin>>a>>b;
     std::string a_str=to_string(a);
     std::string b_str=to_string(b);
     
     std::string str_num=a_str+b_str;
     //cout<<typeid(str_num).name<<endl;
     int number=stoi(str_num);
     
     bool check=false;
     //cout<<typeid(number).name<<endl;
     for(int i;i<number;i++){
         if(i*i==number){
             cout<<"Yes"<<endl;
             check=true;
             break;
         }

             
         }
     if(! check){
         cout<<"No"<<endl;
     }
     }
 