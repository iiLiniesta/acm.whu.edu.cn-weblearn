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

int n,m,a[15][3050];
int work(){
    int tot=1,gray=0;
    int i,j,k,bit,cnt,sum,ans;
    f(i,1,m)tot*=2;
    ans=0;
    f(k,1,tot){
        if(k&1){
            f(j,1,n)a[1][j]=!a[1][j];
            gray^=1;
        }else{
            bit=0;
            while(0==(gray&(1<<bit)))bit++;
            bit++;
            gray^=(1<<bit);
            bit++;
            f(j,1,n)a[bit][j]=!a[bit][j];
        }
        sum=0;
        f(j,1,n){
            cnt=0;
            f(i,1,m)cnt+=a[i][j];
            cnt=max(cnt,m-cnt);
            sum+=cnt;
        }
        //printf("i=%d,\tsum=%d\n",i,sum);
        ans=max(sum,ans);
        if(ans==m*n)break;
    }
    return ans;
}


// -- author: lijw --
int main()
{
    int i,j,ans,tot;
    while(scanf("%d%d",&m,&n)!=EOF){
        f(i,1,m)f(j,1,n)scanf("%d",&a[i][j]);
        ans=work();
        printf("%d\n",ans);
    }

    return 0;
}
