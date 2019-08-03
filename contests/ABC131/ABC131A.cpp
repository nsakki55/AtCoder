#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){

    string str;
    cin>>str;

    vector<int> nums(str.size());

    transform(str.begin(),str.end(),nums.begin(),[](char ch) {return ch- '0';});

    bool flag=true;
    int before_num;

    for(int i=0;i<nums.size();i++){
        if(flag){
            if(i==0) before_num=nums[i];
            else{
                if(nums[i]==before_num){
                    flag=false;
                    cout<<"Bad"<<endl;
                }
                before_num=nums[i];
            }
        }
    }

    if(flag) cout<<"Good"<<endl;

    //for(int i=0;i<nums.size();i++) cout<<nums[i];

    return 0;
}