#include<stdio.h>
#include<string.h>
#define LEN 100005

// Pという変数型を定義
typedef struct pp
{
    char name[100];
    int t;
} P;

P Q[LEN];
int head,tail,n;

void enqueue(P x){
    Q[tail]=x;
    tail=(tail+1)%LEN;
}

P dequeue(){
    P x=Q[head];
    head=(head+1)%LEN;
    return x;
}

int min(int a,int b){
    // ?条件演算子　if 分を簡単に書いている
    return a<b ? a:b;
}

int main(){
    int elaps =0,c;
    int i,q;
    P u;
    scanf("%d %d",&n,&q);

    for( i=1 ; i<=n; i++){
        scanf("%s",Q[i].name);
        scanf("%d",&Q[i].t);
    }
    head=1;tail=n+1;

    while(head !=tail){
        u=dequeue();
        c=min(q,u.t); // q or u.t時間だけ処理を行う
        u.t-=c; //残り時間
        elaps+=c; //経過時間
        if(u.t >0) enqueue(u);
        else{
            printf("%s %d\n",u.name,elaps);
        }
    }
    return 0;
}


