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

#define LEN 200005

int pointer[LEN]={0};
int result[LEN]={0};

int getf(int k)
{
    if(pointer[k]==k){
        pointer[k]++;
        return k;
    }
    return pointer[k]=getf(pointer[k]);
}

int main()
{
    int n,i,t,loc,top=0;
    scanf("%d",&n);
    while(n){
        memset(pointer, 0, LEN);
        memset(result, 0, LEN);
        top=0;
        f(i,1,LEN-1)pointer[i]=i;
        f(i,1,n)
        {
            scanf("%d",&t);
            loc=getf(t);
            if(top<loc)
                top=loc;
            result[loc]=i;
        }
        printf("%d\n",top);
        f(i,1,top-1){
            printf("%d ",result[i]);
        }
        printf("%d\n",result[top]);
        scanf("%d",&n);
    }
    return 0;
}
