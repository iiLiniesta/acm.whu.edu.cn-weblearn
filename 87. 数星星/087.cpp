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
    int n,i,j,k,now,ans;
    float x[500], y[500];
    while(EOF!=scanf("%d", &n)){
        f(i,1,n)scanf("%f %f", &x[i], &y[i]);
        if(n<3){
            printf("%d\n",n);
            continue;
        }
        ans=2;
        f(i,1,n)
            f(j,i+1,n){
                now=2;
                f(k,j+1,n){
                    float dx1,dx2,dy1,dy2;
                    dx1=x[i]-x[j];
                    dx2=x[i]-x[k];
                    dy1=y[i]-y[j];
                    dy2=y[i]-y[k];
                    if(0==dx1*dy2-dy1*dx2)now++;
                }
                if(now>ans)ans=now;
            }
        printf("%d\n",ans);

    }

    return 0;
}
