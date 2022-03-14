#include <stdio.h>
#define MAX 250
int parent(int);
int left(int);
int right(int);

int main()
{
    int i;
    int n;
    int H[MAX + 1];

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        scanf("%d", &H[i]);
    }

    for (i = 1; i <= n; i++)
    {
        printf("node %d: key = %d, ", i, H[i]);
        if (parent(i) >= 1)
            printf("parent key = %d, ", H[parent(i)]);
        if (left(i) <= n)
            printf("left key = %d, ", H[left(i)]);
        if (right(i) <= n)
            printf("right key = %d, ", H[right(i)]);
        printf("\n");
    }

    return 0;
}

int parent(int i)
{
    return i / 2;
}

int left(int i)
{
    return i * 2;
}

int right(int i)
{
    return i * 2 + 1;
}
