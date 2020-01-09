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

#define LEN 100005
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int n,s,i,j;
    int ans[LEN],sz[105],wt[105];
    while(EOF!=scanf("%d", &n)){
        f(i,1,n)scanf("%d %d",&sz[i],&wt[i]);
        scanf("%d",&s);
        f(i,0,s)ans[i]=0;
        f(i,1,n){
            fd(j,s,sz[i]){
                int temp = ans[j-sz[i]]+wt[i];
                if(ans[j]<temp)ans[j]=temp;
                //printf("i=%d, j=%d, temp=%d, wt[j]=%d\n",i,j,temp,wt[j]);
            }
        }
        //f(i,1,s)printf("i=%d, ans[i]=%d\n",i,ans[i]);
        printf("%d\n",ans[s]);
    }

    return 0;
}
