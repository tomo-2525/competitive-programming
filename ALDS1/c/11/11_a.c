#include <stdio.h>
#define N 100
int G[N + 1][N + 1];
int main()
{
    int i, j;
    int n, k, v, u;
    //int G[N+1][N+1];

    scanf("%d", &n);
    G[0][0] = 0;
    for (i = 1; i <= n; i++)
    {
        scanf("%d%d", &u, &k);
        for (j = 1; j <= k; j++)
        {
            scanf("%d", &v);
            G[i][v] = 1;
        }
    }

    for (i = 1; i <= n; i++)
    {
        for (j = 1; j <= n; j++)
        {
            printf("%d", G[i][j]);
            if (j != n)
                printf(" ");
        }
        printf("\n");
    }

    return 0;
}
