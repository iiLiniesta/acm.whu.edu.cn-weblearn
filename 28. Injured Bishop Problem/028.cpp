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

int work(int n,int dx,int dy){
    if(1&(dx+dy))return -1;
    return max(dx,dy);
}

// -- author: lijw --
int main()
{
    int T,n,i,x1,y1,x2,y2,dx,dy,ans;
    scanf("%d", &T);
    f(i,1,T){
        scanf("%d", &n);
        scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
        dx=abs(x1-x2);
        dy=abs(y1-y2);
        ans=work(n,dx,dy);
        printf("Case %d:\n%d\n",i,ans);
        if(i<T)NN;
    }
    return 0;
}
