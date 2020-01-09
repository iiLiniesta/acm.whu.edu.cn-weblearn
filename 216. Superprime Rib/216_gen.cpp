
#include<iostream>
#include<cstdio>
#include<fstream>
#include<cmath>

int N;
int a[]={2,3,5,7};
//判断是否为素数
int prime(int n){
    if(n==2)return 1;
    if(n%2==0)return 0;
    for(int i=3;i*i<=n;i++){
        if(n%i==0)return 0;
    }
    return 1;
}
//从左到右判断
void dfs(int i,int j){
    if(!prime(i)||j>N)return ;//如果i不是素数或者j大于N无返回值
    if(j==N&&prime(i))printf("%d\n",i);//如果是素数且j==N;则打印
    for(int k=1;k<=9;k+=2){//末位为偶数的都不是素数不用考虑
        dfs(i*10+k,j+1);
    }
}
int main(){
    while(scanf("%d",&N))
        for(int i=0;i<4;i++){
            dfs(a[i],1);
        }
}
