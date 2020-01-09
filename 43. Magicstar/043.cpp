
#include<stdio.h>
#include<string.h>
char name[6001][1001];
char n1[1001],n2[1002];
int n,m,q;
int main(){
	int ans,i,j,k;
	scanf("%d",&n);
	while(n--){
		scanf("%d",&i);
		scanf("%s",&name[i]);
	}
	scanf("%d",&m);
	while(m--){
		scanf("%d",&q);
		ans=0;
		while(q--){
			scanf("%d %d",&i,&j);
			for(k=0;name[i][k]!='\0'&&name[j][k]!='\0';k++){
				if(name[i][k]!=name[j][k])
				break;
			}
			ans+=k;
		}
		printf("%d\n",ans);
	}
	return 0;
} 
