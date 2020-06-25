#include <stdio.h>
#include <string.h>
#define N 10000

int LCSLength(char *, char *);

char X[N + 1], Y[N + 1];
int c[N + 1][N + 1];

int main()
{

    int q;
    int i;
    scanf("%d", &q);

    for (i = 0; i < q; i++)
    {
        X[0] = ' ';
        Y[0] = ' ';
        scanf(" %s %s", &X[1], &Y[1]);

        // printf("%s\n%s\n",X,Y);

        printf("%d\n", LCSLength(X, Y));
    }

    return 0;
}

int LCSLength(char *X, char *Y)
{
    int i, j;
    int m, n;
    m = strlen(X);
    n = strlen(Y);

    for (i = 1; i <= m; i++)
    {
        c[i][0] = 0;
    }

    for (j = 0; j <= n; j++)
    {
        c[0][j] = 0;
    }

    for (i = 1; i <= m; i++)
    {
        for (j = 1; j <= n; j++)
        {
            if (X[i] == Y[j])
            {
                c[i][j] = c[i - 1][j - 1] + 1;
            }
            else if (c[i - 1][j] >= c[i][j - 1])
            {
                c[i][j] = c[i - 1][j];
            }
            else
                c[i][j] = c[i][j - 1];
        }
    }

    return c[m][n] - 1;
}
