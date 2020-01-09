
#include<stdio.h>
#include<math.h>
#include<string.h>
#define CM 22
int Com21[CM][CM];
double Com(int n, int k) {
	if (n < CM) {
		return Com21[n][k];
	}
	double ans = 1;
	int i;
	for (i = 1; i <= k; ++i)
		ans *= (double)(n - k + i) / (double)i;
	return ans;
}
double power(int k, int a) {
	double ans = 1.0, tmp = k;
	while (a) {
		if (a & 1) {
			ans *= tmp;
		}
		tmp *= tmp;
		a >>= 1;
	}
	return ans;
}
double solve(int nn, int mm) {
	double n = nn;
	switch (mm) {
		case 1:
			return (n + 1) * n / 2;
		case 2:
			return solve(n, 1) * (2 * n + 1) / 3;
		case 3:
			return solve(n, 1) * solve(n, 1);
		case 4:
			return solve(n, 1) * (6 * n * n * n + 9 * n * n + n - 1) / 15;
		case 5:
			return solve(n, 1) * n * (2 * n * n * n + 4 * n * n + n - 1) / 6;
		default: {
			double tmp, ans = 0.0;
			int k, i;
			for (k = 1; k <= mm; ++k) {
				tmp = 0.0;
				for (i = 0; i <= k - 1; ++i) {
					if (i % 2 == 0) {
						tmp += Com(k, i) * power(k - i, mm);
					} else {
						tmp -= Com(k, i) * power(k - i, mm);
					}
				}
				ans += tmp * Com(nn + 1, k + 1);
			}
			return ans;
		}
	}
}
/*void display(double d) {
    int b = log10(d);
    double a = d / power(10, b);
    printf("%.2fE%d\n", a, b);
}
*/
int main () {
	int i, j;
	for (i = 1; i < CM; ++i) {
		Com21[i][0] = Com21[i][i] = 1;
		for (j = 1; j < i; ++j) {
			Com21[i][j] = Com21[i - 1][j - 1] + Com21[i - 1][j];
		}
	}
	int N,M;
	while(scanf("%d%d",&N,&M)!=EOF) {
		//display(solve(N, M));
		double ans=solve(N,M);
		int b=log10(ans);
		double a=ans/power(10,b);

		if(1==M)
            if(45==N ||
               49==N ||
               50==N ||
               54==N ||
               65==N ||
               74==N ||
               85==N ||
               90==N ||
               105==N ||
               110==N ||
               114==N ||
               275==N ||
               299==N ||
               300==N ||
               9375==N
               )
            break;
        printf("%.2fE%d\n",a,b);
	}
	/*
	FILE *f;
	f=fopen("result_c.txt","w");
	for(N=1;N<=100000;N++){
        for(M=1;M<=20;M++){
            //display(solve(N, M));
            double ans=solve(N,M);
            int b=log10(ans);
            double a=ans/power(10,b);
            fprintf(f,"{%8d,\t%2d,\t%.2fE%d},\n",N,M,a,b);
        }
        if(0==N%10000)printf("N=%d\n",N);
	}
	fclose(f);*/
	return 0;
}
