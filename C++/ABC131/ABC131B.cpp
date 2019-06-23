#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;


int main(){
    int n,l;
    cin>>n>>l;


    vector<int> taste(n);

    for(int i=0;i<n;i++) taste[i]=l+i;
    
    int total_n=0;
    for(int i=0;i<n;i++) total_n+=taste[i];

    bool flag=true;
    int pick=1000;
    int index;
    

    for(int i=0;i<n;i++){
        if(flag){
           if(taste[i]==0){
           pick=0;
           index=i; 
           flag=false;
         }
           else{
               pick=min(abs(taste[i]),pick);
               if(abs(taste[i])==pick){
                   index=i;
               } 
           }
        }
    }

    int sum=0;
    for(int i=0;i<n;i++){
        if(i!=index){ 
        sum+=taste[i];
        }
    }
    cout<<sum<<endl;
   // cout<<index<<endl;
   // for(int i=0;i<n;i++) cout<<taste[i];
    
    return 0;
}