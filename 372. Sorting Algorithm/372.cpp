#include<cstdio>
#include<algorithm>
using namespace std;
int num[100007];
int m,n;
int main(){
	int i,j,k;
	while(scanf("%d %d",&n,&m)!=EOF){
		if(n==0&&m==0)break;
		for(i=0;i<n;i++)
		scanf("%d",&num[i]);
		sort(num,num+n);
		for(i=0;i<n;i=i+m){
			if(i==0)
			printf("%d",num[i]);
			else
			printf(" %d",num[i]);
		}
		printf("\n");
	}
	return 0;
}
