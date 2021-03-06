#include<stdio.h>
#include<iostream>
 
using namespace std;
 
#define BUF_SIZE 1024
 
class Stack{
public:
    Stack(int stack_size):
        m_index(0){
        m_array = new int[stack_size];
    };
    ~Stack(){
        delete[] m_array;
    };
    void push(int var){
        m_array[m_index++] = var;
    };
    int pop(){
        return m_array[--m_index];
    };
 
    bool isEmpty(){
        return m_index == 0;
    };
 
private:
    int* m_array;
    int m_index;
};
 
int main(){
    char buf[BUF_SIZE];
 
    for(int i = 0; i < BUF_SIZE; i++){
        buf[i] = 'e';
    }
    fgets(buf,BUF_SIZE,stdin);
 
    Stack stack(BUF_SIZE);
 
    bool numFLG = false;
    int S = 0,op1=0,op2=0;
 
    for(int i = 0;buf[i] != 'e'; i++){
        if(buf[i] >= '0' && buf[i] <= '9'){
            numFLG = true;
            S = 10*S + (buf[i] - '0');
        }else{
            if(numFLG){
                stack.push(S);
                S = 0;
                numFLG = false;
            }
 
            if(buf[i] == '+'){
                op2 = stack.pop();
                op1 = stack.pop();
                stack.push(op1+op2);
            }else if(buf[i] == '-'){
                op2 = stack.pop();
                op1 = stack.pop();
                stack.push(op1-op2);
            }else if(buf[i] == '*'){
                op2 = stack.pop();
                op1 = stack.pop();
                stack.push(op1*op2);
            }
        }
    }
 
    op1 = stack.pop();
    printf("%d\n",op1);
}