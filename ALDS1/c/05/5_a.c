#include <stdio.h>
#define true 1
#define false 0

int judge(int, int);
int A[25], Q[205];
int n, q, sum = 0, flag = 0;

int main()
{

    int i, j;

    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        scanf("%d", &A[i]);
    }

    scanf("%d", &q);
    for (i = 0; i < q; i++)
    {
        scanf("%d", &Q[i]);
    }

    for (j = 0; j < q; j++)
    {
        if (judge(0, Q[j]) == true)
            printf("yes\n");
        else
            printf("no\n");
    }

    return 0;
}

int judge(int i, int m)
{
    //printf("%d %d\n",i,m);
    int res = false;

    if (m == 0)
        return true;

    if (i >= n)
        return false;

    if (judge(i + 1, m - A[i]) == true)
        res = true;
    if (judge(i + 1, m) == true)
        res = true;

    return res;
}
