#include <stdio.h>
#include <limits.h>
#define N 100

void matrixChainOrder(int, int *);
int min(int, int);

int M[N + 1][N + 1];

int main()
{

    int n;
    int P[N + 1];
    int i;

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        scanf("%d%d", &P[i - 1], &P[i]);
    }
    //printf("\n");
    for (i = 0; i <= n; i++)
    {
        //  printf("%d ",P[i]);
    }

    matrixChainOrder(n, P);
    //printf("\n");
    printf("%d\n", M[1][n]);

    return 0;
}

void matrixChainOrder(int n, int *p)
{
    int i, l, k, q, j;
    int INF = INT_MAX;
    //n = n -1;//p.length -1

    for (i = 1; i < n; i++)
    {
        M[i][i] = 0;
    }

    for (l = 2; l <= n; l++)
    {
        for (i = 1; i <= n - l + 1; i++)
        {
            j = i + l - 1;
            M[i][j] = INF;

            for (k = i; k <= j - 1; k++)
            {
                q = M[i][k] + M[k + 1][j] + p[i - 1] * p[k] * p[j];
                M[i][j] = min(M[i][j], q);
            }
        }
    }
}

int min(int a, int b)
{
    if (a < b)
        return a;
    else
        return b;
}
