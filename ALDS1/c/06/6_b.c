#include <stdio.h>
#include <stdlib.h>

int main()
{

    int n, A[100005];
    int i, j, k, cmp, tmp;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &A[i]);
    }
    cmp = A[n - 1];

    i = 0;

    for (j = 0; j < n - 1; j++)
    {
        if (A[j] <= cmp)
        {
            tmp = A[i];
            A[i] = A[j];
            A[j] = tmp;
            i++;
        }

        for (k = 0; k < n; k++)
        {
            // printf("%-5d",A[k]);
        }
        //printf("\n");
    }
    tmp = A[i];
    // printf("値tmp:%d",A[i]);
    A[i] = cmp;
    A[n - 1] = tmp;

    for (k = 0; k < n; k++)
    {
        if (k == i)
            printf("[%d]", A[k]);
        else
            printf("%d", A[k]);
        if (k != n - 1)
            printf(" ");
    }

    printf("\n");

    return 0;
}
