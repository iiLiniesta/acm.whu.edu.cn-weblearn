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

#define LEN 300005
#define INF 0x7fffffff

vector<int> mapa[LEN];
int dist[LEN]={0};

bool relax(int u,int v)
{
    if(dist[u]+1<dist[v]){
        dist[v]=dist[u]+1;
        return true;
    }
    return false;
}


void spfaaa(int start)
{
    int visited[LEN]={0};
    memset(visited,0,sizeof(visited));
    visited[start]=1;
    dist[start]=0;
    int now,i;
    queue<int> Q;
    Q.push(start);
    while(!Q.empty())
    {
        now=Q.front();
        Q.pop();
        //f(i,0,mapa[now].size()-1){ # Fail if using this line instead the following one.
        for(i=0;i<mapa[now].size();i++){
            if(relax(now,mapa[now][i])){
                if(0==visited[mapa[now][i]]){
                    Q.push(mapa[now][i]);
                    visited[mapa[now][i]]=1;
                }
            }
        }
        visited[now]=0;
    }
}

// -- author: lijw --
int main()
{
    int n,m,i,k,x,y,j;
    scanf("%d %d",&n,&m);

    f(i,0,LEN-1)mapa[i].clear();
    f(i,1,m){
        scanf("%d %d",&x,&y);
        mapa[x].push_back(y);
        mapa[y].push_back(x);
    }
    scanf("%d",&k);
    f(j,1,k){
        f(i,0,LEN-1)dist[i]=INF;
        scanf("%d %d",&x,&y);
        if(x==y){
            puts("0");
            continue;
        }

        spfaaa(x);
        if(dist[y]==INF)puts("-1");
        else printf("%d\n", dist[y]-1);
    }

    return 0;
}
