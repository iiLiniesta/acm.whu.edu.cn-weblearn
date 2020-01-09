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

int score(double x, double y){
//    double r=x*x+y*y;
//	if(r<=3*3)
//        return 100;
//	else if(r<=6*6)
//        return 80;
//	else if(r<=9*9)
//        return 60;
//	else if(r<=12*12)
//        return 40;
//	else if(r<=15*15)
//        return 20;
//	else
//        return 0;

    int r=3;
    double d2 = x * x + y * y;
    while(r * r < d2 && r <= 15)r += 3;
    int ans = (6-(r/3)) * 20;
    return ans;
}
double s[12];
int work(){
    int a1=0, a2=0;
    a1=score(s[0],s[1])+score(s[2],s[3])+score(s[4],s[5]);
    a2=score(s[6],s[7])+score(s[8],s[9])+score(s[10],s[11]);
    if(a1>a2)printf("SCORE: %d to %d, PLAYER 1 WINS.\n", a1, a2);
    else if(a1<a2)printf("SCORE: %d to %d, PLAYER 2 WINS.\n", a1, a2);
    else if(a1==a2)printf("SCORE: %d to %d, TIE.\n", a1, a2);
}


// -- author: lijw --
int main()
{
    while(true){
        scanf("%lf %lf %lf %lf %lf %lf %lf %lf %lf %lf %lf %lf",&s[0],&s[1],&s[2],&s[3],&s[4],&s[5],&s[6],&s[7],&s[8],&s[9],&s[10],&s[11]);
        if(s[0]==-100.0)break;
        work();
    }

    return 0;
}
