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

#define LEN 1000010
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int n, i, counter, ans,now;
    while(scanf("%d",&n)!=EOF){
        counter=1;
        scanf("%d", &ans);
        f(i,2,n){
            scanf("%d", &now);
            if(now==ans)counter++;
            else counter--;
            if(counter<=0){
                counter=1;
                ans=now;
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

