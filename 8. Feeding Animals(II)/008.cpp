#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<queue>

using namespace std;

#define f(i,a,b) for(i=(a);i<=(b);i++)
#define fd(i,a,b) for(i=(a);i>=(b);i--)
#define fff(i,a,b,k) for(i=(a);i<=(b);i+=k)
#define fffd(i,a,b,k) for(i=(a);i>=(b);i-=k)
#define NN printf("\n")
#define TT printf("\t")
#define SP printf(" ")

#define LEN 11000
#define INF 0x7fffffff

vector<int> mapa[LEN];
int pre[LEN],used[LEN];

int dfs(int k)
{
    int i;
    for(i=0;i<mapa[k].size();++i){
        if(used[mapa[k][i]] == 0){
            used[mapa[k][i]] = 1;
            if(pre[mapa[k][i]] == 0 || dfs(pre[mapa[k][i]])){
                pre[mapa[k][i]]=k;
                return 1;
            }
        }
        else continue;
    }
    return 0;
}

// -- author: lijw --
int main()
{
    int m,n,i,j,h,k,temp,ans;
    int a[LEN],matrix[105][105];
    while(EOF!=scanf("%d %d",&m,&n)){
        f(i,1,m)f(j,1,n)scanf("%d",&matrix[i][j]);
        scanf("%d",&k);
        if(k>n)k=n;

        f(i,1,LEN)mapa[i].clear();
        memset(pre,0,sizeof(pre));

        int now=n;
        // 1 to n: animals
        // now_i to now_i+k-1 the i-th person's capability
        f(i,1,m){
            f(h,now+1,now+k){
                f(j,1,n)if(matrix[i][j]){
                    mapa[h].push_back(j);
                    mapa[j].push_back(h);
                    //printf("h=%d, j=%d\n",h,j);
                }
            }
            now+=k;
        }

        int tot=now;
        /*
        f(i,1,tot){
            printf("i=%d:\n",i);
            for(j=0;j<mapa[i].size();j++){
                printf("%d\t",mapa[i][j]);
            }
            NN;
        }
        */

        int ans=0;
        for(i=1;i<=n;++i)
        {
            memset(used,0,sizeof(used));
            if(dfs(i))ans++;
        }
        if(ans==n)printf("Yes\n");
        else printf("No\n");

    }

    return 0;
}
