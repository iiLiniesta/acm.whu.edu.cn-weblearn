
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
using namespace std;
int n,m,k,dist[200002];
vector<int> g[200002];

inline bool relax(int u,int v)
{
    if(dist[u]+1<dist[v])
    {
        dist[v]=dist[u]+1;
        return true;
    }
    return false;
}

void spfa(int s)
{
    int vis[n+5];
    memset(vis, 0, sizeof(vis));
    queue<int> q;
    q.push(s);
    vis[s] = true;
    dist[s] = 0;
    while(!q.empty())
    {
        int temp=q.front();
        q.pop();
        for(int i=0;i<g[temp].size();i++)
            if(relax(temp, g[temp][i])&&!vis[g[temp][i]])
            {
                q.push(g[temp][i]);
                vis[g[temp][i]]=true;
            }
        vis[temp] = false;
    }
}

int main()
{
    int a,b,i,loop;
    scanf("%d %d", &n, &m);
    for(i=0;i<n;i++)
	g[i].clear();
    for(i=0;i<m;i++){
        scanf("%d %d", &a, &b);
        g[a].push_back(b);
        g[b].push_back(a);
    }
    scanf("%d",&k);
    for(loop=0;loop<k;loop++){
        for(i=0;i<n;i++)
		dist[i] = 0x7fffffff;
        scanf("%d %d", &a, &b);
        if(a == b){
			puts("0");
			continue;
		}
        spfa(a);
        if(dist[b]==0x7fffffff) puts("-1");
        else printf("%d\n", dist[b]-1);
    }
    return 0;
}
