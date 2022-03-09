#include <stdio.h>
#include <limits.h>
#define U 10000
#define NIL -1
#define WHITE 0
#define BLACK 1
#define MAX 100009
int d[U];
int parent[U];
int color[U];

int main()
{
    int cost = 0;
    int mincost;
    int i, j, k, u, v;
    int n, c;
    int A[105][105];
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            A[i][j] = NIL;
        }
    }

    for (i = 0; i < n; i++)
    {
        scanf("%d%d", &u, &k);
        for (j = 0; j < k; j++)
        {
            scanf("%d%d", &c, &v);
            A[u][c] = v;
        }
    }

    for (u = 0; u < n; u++)
    {
        d[u] = MAX; //コスト おもさ
        parent[u] = NIL;
        color[u] = WHITE; //訪問した:BLACK   訪問まだ:WHITE
    }
    d[0] = 0; //最初の島のコストは０

    while (1)
    {
        mincost = MAX;

        for (i = 0; i < n; i++)
        {
            if (color[i] != BLACK && d[i] < mincost)
            {
                mincost = d[i];
                u = i;
            }
        }

        // printf("aiueo\n");

        if (mincost == MAX)
            break;

        color[u] = BLACK;

        for (v = 0; v < n; v++)
        {
            if (color[v] != BLACK && A[u][v] + d[u] < d[v] && A[u][v] != NIL)
            {
                parent[v] = u;
                d[v] = A[u][v] + d[u];
            }
        }
    }

    for (v = 0; v < n; v++)
        cost += d[v];

    //  printf("%d\n",cost);

    for (i = 0; i < n; i++)
    {
        printf("%d %d\n", i, d[i]);
    }

    return 0;
}
