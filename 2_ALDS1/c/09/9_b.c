#include <stdio.h>
#define MAX 500000

int H[MAX + 1];

void maxHeepify(int, int);
void buildMaxHeep(int);
void swap(int, int);

int main()
{
    int i;
    int n;

    scanf("%d", &n);
    for (i = 1; i <= n; i++)
    {
        scanf("%d", &H[i]);
        // printf(" %d",H[i]);
    }

    buildMaxHeep(n);

    for (i = 1; i <= n; i++)
    {
        printf(" %d", H[i]);
    }

    printf("\n");

    return 0;
}

void maxHeepify(int i, int n)
{
    int l, r;
    int largest;

    l = i * 2;
    r = i * 2 + 1;
    //左の子、自分、右の子で値が最大のノードを選ぶ

    if (l <= n && H[l] > H[i])
        largest = l;
    else
        largest = i;

    if (r <= n && H[r] > H[largest])
        largest = r;

    if (largest != i)
    {
        swap(i, largest);
        maxHeepify(largest, n);
    }
}

void buildMaxHeep(int n)
{
    int i;

    for (i = n / 2; i >= 1; i--)
    {
        maxHeepify(i, n);
    }
}

void swap(int a, int b)
{

    int tmp;
    tmp = H[a];
    H[a] = H[b];
    H[b] = tmp;
}
