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

#define LEN 3005
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int t,n,i,j,ans;
    int a[LEN];
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        f(i,1,n)scanf("%d",&a[i]);
        ans = 0;
        f(i,1,n)f(j,i+1,n)
            if(a[i]>a[j])ans++;
        printf("%d\n",ans);
    }

    return 0;
}
