#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int A, B;
  cin >> A >> B;
 
  // ここにプログラムを追記
  int a=0;
  while(a<A){
    if(a==A-1){
    	cout<<"["<<endl;
    }
    if(a==0){
      cout<<"A:[";
    }
    else{
      cout<<"[";
    }
  		a+=1;
}
  
    int b=0;
  while(b<B){
        if(b==B-1){
    	cout<<"["<<endl;
    }
    if(b==0){
      cout<<"B:[";
    }
    else{
      cout<<"[";
    }
  		b+=1;
    }
}
