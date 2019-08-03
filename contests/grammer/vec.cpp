#include<vector>
#include<bits/stdc++.h>
using namespace std;

int main(){
// 要素の値がすべえ5で長さ10の配列を作成
    vector<int> data(10,5);
    int org_data[]={4,6,5};
    vector<int> data2(org_data,org_data+3);
//要素の値を指定して初期化
  //  vector<int> data2{4,5,6};
   // vector<int> x(data2);

// 2次元配列
    vector<vector<int>> vv{{1,2,3},{4,5,6}};

    vector<char> str;
    vector<double> pos(3);
    vector<char> a(10,'a');

    vector<double> d{1.1,2.2,3.3,4.4};
    vector<double> y(d);
    for(int i=0;i<4;i++) cout<<y.at(i)<<endl;
    auto itr=y.begin();
    cout<<*itr<<endl;
    itr++;
    *itr=9.9;
    cout<<*itr<<endl;

   // vector<int> data3(100);
    //for(int i=0;i<100;i++)
   //     data3[i]=rand() %100;
   // for(int i=0;i<100;i++)
   //     cout<<data3[i]<<'\n';

   vector<int> v;
   v.push_back(21);
   cout<<v.at(0)<<endl;

   vector<int> v2(10,3);
   v2.insert(v2.begin()+3,7);
   for(int i=0;i<10;i++) cout<<v2[i];
   vector<int> back;
   for(int i=0;i<10;i++)
   back.push_back(i);
   cout<<back.at(1)<<endl;

   vector<int> v3{1,2,3,4,5};
   int last=v3.back();
   cout<<last<<endl;
   //v3.pop_back();
   for(int i=0;i<3;i++) cout<<v3.at(i); 
   v3.erase(v3.begin()+2);
   for(int i=0;i<v3.size();i++) cout<<v3.at(i);

    cout<<endl;

   vector<int> v4{1,2,3,4,5,6};
   //v4.erase(v4.begin()+1,v3.begin()+5);
   //for(int i=0;i<v4.size();i++) cout<<v4.at(i);
   cout<<!v4.empty()<<endl;
   cout<<v4.size()<<endl;
   cout<<v4.capacity()<<endl;
   cout<<v4.front()<<endl;
   cout<<v4.back()<<endl;
 //  v4.clear();
   cout<<v4.empty()<<endl;
   cout<<v4.size()<<endl;
   cout<<v4.capacity()<<endl; 
   v4.reserve(1);
   cout<<v4.empty();

    vector<int> v5{3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5};
    auto it=find(v5.begin(),v5.end(),9);
    cout<<*it<<endl;
    reverse(v5.begin(),v5.end());
    //sort(v5.begin(),v5.end());
    for(int i=0;i<v5.size();i++) cout<<v5[i];

    return 0;





}