#include <bits/stdc++.h>
using namespace std;
#include <vector>

int main(){

    int n,d;
    cin>>n>>d;

    vector<vector<int>> X(n,vector<int>(d));
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            cin>>X[i][j];
        }
    }

    int ans=0;

    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            int norm=0;
            for(int k=0;k<d;k++){
                int diff=abs(X[i][k]-X[j][k]);
                norm +=diff*diff;
            }
            bool flag=false;
            for(int k=0;k<=norm;++k){
                if(k*k==norm){
                flag=true;
            }
        }
        if(flag) ++ans;
     }
}

cout<<ans<<endl;

return 0;
}