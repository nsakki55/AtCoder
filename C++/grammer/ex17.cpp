#include <bits/stdc++.h>
using namespace std;
 
 int main(){
     int N,S;
     cin>>N>>S;

    vector<int> A(N),B(N);

    for(int i=0;i<A.size();i++){
        cin>>A.at(i);
    }

    for(int i=0;i<B.size();i++){
        cin>>B.at(i);
    }
 
    int count=0;
    for(int i=0;i<A.size();i++){
        for(int j=0;j<B.size();j++){
          //  cout<<A.at(i)<<endl;
            if(A.at(i)+B.at(j)==S)         
               count++;
            }
        }
    cout<<count<<endl;  
    }
    
 
