#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

#define f(i,a,b) for(i=(a);i<=(b);i++)
#define fd(i,a,b) for(i=(a);i>=(b);i--)
#define fff(i,a,b,k) for(i=(a);i<=(b);i+=k)
#define fffd(i,a,b,k) for(i=(a);i>=(b);i-=k)
#define NN printf("\n")
#define TT printf("\t")
#define SP printf(" ")

#define LEN 0
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int a,b,h,T;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d%d",&a,&b,&h);
        printf("%.2f\n",(h*1.0)*(b*1.0)/(a*1.0));
    }

    return 0;
}
