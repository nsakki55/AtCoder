#include <iostream>
using namespace std;

class Car{
    private:
    int num;
    double gas;

    public:
        static int sum;
        Car(int n=0,double g=0);
        void setCar(int n,double g);
        void show();
        static void showSum();
};


Car::Car(int n,double g)
{
    num=n;
    gas=g;
    sum++;
    cout<<"車を購入\n";
    
}

void Car::show(){
    cout<<"num:"<<num<<"\n";
    cout<<"gas:"<<gas<<"\n";
}

void Car::setCar(int n,double g)
{
    num=n;
    gas=g;
    cout<<"num:"<<num<<"gas:"<<gas<<"\n";
}


void Car::showSum()
{
    cout<<"車は全部で"<<sum<<"\n";
}




int Car::sum=0;

int main(){
    
    Car::showSum();
    
    Car car1;
    car1.setCar(12,4.5);

    Car::showSum();

    Car car2(12,3.5);
    Car::showSum();

    return 0;
    

    
}

