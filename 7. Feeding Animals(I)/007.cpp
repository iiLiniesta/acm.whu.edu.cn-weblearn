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

#define LEN 10005
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int n,i,j,k,temp,ans;
    int a[LEN];
    while(EOF!=scanf("%d",&n)){
        f(i,1,n)a[i]=INF;
        f(j,1,8)f(i,1,n){
            scanf("%d",&temp);
            if(temp<a[i])a[i]=temp;
        }
        ans=0;
        f(i,1,n)ans+=a[i];
        printf("%d\n",ans);
    }
    return 0;
}
