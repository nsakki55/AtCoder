#include<bits/stdc++.h>
using namespace std;

int sum_range(int a,int b){
    if(b==a){
        return a;
    }
    return sum_range(a,b-1)+b;
}

int array_sum_from_i(vector<int> &data,int i){
    if(i==data.size()){
        return 0;
    }
    int s=array_sum_from_i(data,i+1);
    return data.at(i)+s;
    }

int array_sum(vector<int> &data){
    return array_sum_from_i(data,0);
}

bool has_divisor(int N,int i){
    if(i==N){
        return false;
    }
    if(N%i==0){
        return true;
    }
    return has_divisor(N,i+1);
    }

bool is_prime(int N){
    if(N==1){
        return false;
    }
    else if(N==2){
        return true;
    }
    else{
        return !has_divisor(N,2);
    }
}

int main(){
    cout<<sum_range(0,4)<<endl;
    cout<<sum_range(5,8)<<endl;

    vector<int> a={0, 3, 9, 1, 5};
    cout<<array_sum(a)<<endl;

      cout << is_prime(1) << endl;  // 0
  cout << is_prime(2) << endl;  // 1
  cout << is_prime(12) << endl; // 0
  cout << is_prime(13) << endl; // 1
  cout << is_prime(57) << endl; // 0
}