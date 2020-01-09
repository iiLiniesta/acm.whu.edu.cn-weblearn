#include<stdio.h>
#include<string.h>
char s1[2005],s2[2005];
int len1,len2;
int main(){
	int t,i,j,k,ans;
	scanf("%d",&t);
	while(t--){
		ans=0;
		scanf("%s %s",&s1,&s2);
		len1=strlen(s1);len2=strlen(s2);
		for(i=0;i<len1;i++){
			if(len1-i<=ans)
			break;
			for(j=0;j<len2;j++){
				if(s1[i]==s2[j]){
					k=1;
					while(s1[i+k]!='\0'&&s2[j+k]!='\0'&&s1[i+k]==s2[j+k])
					k++;
					if(ans<k)
					ans=k;
				}
			}
		}
		printf("%d\n",ans);
	}
	return 0;
}
