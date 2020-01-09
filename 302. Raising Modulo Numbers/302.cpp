#include<iostream>
#include<stdio.h>
#include<string.h>
using namespace std;

int fun(long long int a,long long int b,long long int p)
{
    long long int res=1;
    while(b)
    {
        if(b&1) res=res*a%p;
        a=a*a%p;
        b>>=1;
    }
    return res;
}
int main()
{
    long long int t;
    long long int a,b,h,p;
    scanf("%lld",&t);
    while(t--)
    {
        long long int ans=0;
        scanf("%lld%lld",&p,&h);
        for(int i=1;i<=h;i++)
        {
            scanf("%lld%lld",&a,&b);
            ans=ans+fun(a,b,p);

        }
        ans=ans%p;
        printf("%I64d\n",ans);
    }
    return 0;
}