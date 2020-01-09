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
    int n, i, x, ans;
    scanf("%d", &n);
    ans=0;
    f(i,1,2*n+1){
        scanf("%d", &x);
        ans ^= x;
    }
    printf("%d\n", ans);

    return 0;
}
