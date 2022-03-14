#include <stdio.h>
#include <stdlib.h>
#define N 8
#define FREE 0
#define NOT_FREE 1

int row[N], col[N], dpos[N * 3], dneg[N * 3]; //すべてFREEの状態
int row2[N];

int putQueen(int);
void printBord(void);

int main()
{
    int i, j;
    int k, r, c;

    scanf("%d", &k);

    for (i = 0; i < N; i++)
        row2[i] = -1;
    for (i = 0; i < k; i++)
    {
        scanf("%d%d", &r, &c);
        row[r] = c;
        col[c] = NOT_FREE;
        dpos[r + c] = NOT_FREE;
        dneg[r - c + N - 1] = NOT_FREE;
        row2[r] = c;
    }

    putQueen(0);
    //printBord();

    return 0;
}

int putQueen(int i)
{

    int j;
    // printBord();
    // printf("\n");
    if (i == N)
    {
        printBord();
        return 0;
        //exit(3);
    }

    if (row2[i] != -1)
    {
        putQueen(i + 1);
        return 0;
    }

    for (j = 0; j <= N - 1; j++)
    {
        // printf("i=%d j=%d, row2[%d] = %d\n", i, j, i, row2[i]);
        //	printf("%d %d %d\n", col[j], dpos[i+j], dneg[i-j+N-1]);
        if (col[j] == NOT_FREE || dpos[i + j] == NOT_FREE || dneg[i - j + N - 1] == NOT_FREE)
        {
            continue;
        }

        /*
    if(row2[i] == 1 ){
      if(putQueen(i+1))return 1;
      return 2;
    }
    */

        //put a queen at(i,j)
        row[i] = j;
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = NOT_FREE;

        //try the next row
        putQueen(i + 1);

        //remove the queen at (i,j) for backtracking
        col[j] = dpos[i + j] = dneg[i - j + N - 1] = FREE;
    }

    return 0;
}

void printBord()
{

    //チェス板を出力
    int i, j;
    for (i = 0; i < N; i++)
    {
        for (j = 0; j < N; j++)
        {
            if (j == row[i])
                printf("Q");
            else
                printf(".");
        }
        printf("\n");
    }
}
