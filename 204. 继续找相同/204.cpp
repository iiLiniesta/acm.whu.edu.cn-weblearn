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

#define LEN 500005
#define INF 0x7fffffff

// -- author: lijw --
int main()
{
    int n, i, mid, ans,now,s[LEN];
    while(scanf("%d",&n)!=EOF){
        f(i,0,n-1)scanf("%d", &s[i]);
        mid = n >> 1;
        sort(s,s+n);
        if(n&1 || (0==n&1 && s[mid]==s[mid-1])){
            printf("%d\n", s[mid]);
            continue;
        }
        if(s[n-1]==s[mid])printf("%d\n", s[mid]);
        else printf("%d\n", s[mid-1]);
    }
    return 0;
}

