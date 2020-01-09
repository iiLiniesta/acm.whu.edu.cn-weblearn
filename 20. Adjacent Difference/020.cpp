#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>

using namespace std;

#define f(i,a,b) for(i=a;i<=b;i++)
#define fd(i,a,b) for(i=a;i>=b;i--)
#define fff(i,a,b,k) for(i=a;i<=b;i+=k)
#define fffd(i,a,b,k) for(i=a;i>=b;i-=k)
#define NN printf("\n")
#define TT printf("\t")
#define SP printf(" ")

int comp(const void*a,const void*b){
	return *(int*)a-*(int*)b;
}

void work()
{
    int n,j;
    int a[1005],b[1005];
    a[0]=0;

    scanf("%d",&n);
    f(j,1,n)
    {
        scanf("%d",&a[j]);
        b[j]=a[j]-a[j-1];
    }
    qsort(b+1,n,sizeof(int),comp);
    f(j,1,n-1)printf("%d ",b[j]);
    printf("%d",b[n]);
}

int main()
{
    int T,i;
    scanf("%d",&T);
    if(0==T)return 0;
    f(i,1,T-1)
    {
        printf("Case %d:\n",i);
        work();
        NN;NN;
    }
    printf("Case %d:\n",T);
    work();

    return 0;
}
