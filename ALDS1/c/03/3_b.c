#include <stdio.h>
#include <string.h>

#define LEN 100005

typedef struct
{
    char name[100];
    int time;
} DATA;

void enqueue(DATA);
DATA dequeue();

int head = 0, tail = 0;
DATA data[LEN + 1];

int main()
{

    int elaps = 0, t, i, n, q, flag = 0;
    DATA tmp;
    scanf("%d%d", &n, &q);

    for (i = 0; i < n; i++)
    {
        scanf("%s %d", tmp.name, &tmp.time);
        enqueue(tmp);
    }

    while (1)
    {
        // printf("経過時間:%d\n",elaps);

        tmp = dequeue();
        if (q < tmp.time)
            t = q;
        else
            t = tmp.time;
        tmp.time -= t;
        elaps += t;

        if (tmp.time > 0)
            enqueue(tmp);
        else
            printf("%s %d\n", tmp.name, elaps);

        if (head == tail)
            break;
    }

    return 0;
}

void enqueue(DATA x)
{
    if (tail == LEN)
        tail = 0;
    strcpy(data[tail].name, x.name);
    data[tail].time = x.time;
    tail++;
}

DATA dequeue()
{
    if (head == LEN)
        head = 0;
    head++;
    return data[head - 1];
}
