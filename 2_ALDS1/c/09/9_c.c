#include <stdio.h>
#include <limits.h>
#define MAX 20000000
#define NIL INT_MIN

void maxHeepify(int, int);
void buildMaxHeep(int);
void swap(int, int);
void insert(int);
int extract(void);
void heepIncreasekey(int, int);
int H[MAX + 1];
int n;

int main()
{
    int i;
    int key;
    int cnt = 0;
    char order[10];

    while (1)
    {

        scanf("%s", order);
        if (order[0] == 'i')
        { //挿入
            scanf("%d", &key);
            insert(key);
            //cnt++;
            //printf("111111\n");
        }
        else if (order[1] == 'x')
        { //取出し
            //cnt--;
            // printf("222222222\n");
            printf("%d\n", extract());
        }

        if (order[2] == 'd')
            break; //終了
    }

    for (i = 1; i <= cnt; i++)
    {
        //printf("%d",H[i]);
    }
    //printf("\n");

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
/*
void buildMaxHeep(int n){
  int i;

  for(i=n/2 ; i >= 1 ; i--){
    maxHeepify(i,n);
  }
  
}
*/
void swap(int a, int b)
{

    int tmp;
    tmp = H[a];
    H[a] = H[b];
    H[b] = tmp;
}

int extract(void)
{
    int maxv;
    maxv = H[1];
    H[1] = H[n];
    n--;
    maxHeepify(1, n);
    return maxv;
}

void insert(int key)
{
    n++;
    H[n] = NIL;
    heepIncreasekey(n, key);
}

void heepIncreasekey(int i, int key)
{

    if (key < H[i])
        return;
    H[i] = key;
    while (i > 1 && H[i / 2] < H[i])
    {
        swap(i, i / 2);
        i = i / 2;
    }
}
