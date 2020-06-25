#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void push(int);
void calc(char);

int top = 1;
int s[100];

int main()
{

    char num[4];
    int i, tmp, flag = 0;

    while (1)
    {
        if (scanf("%s", num) == EOF)
            break;

        flag = 0;
        for (i = 0; i < strlen(num); i++)
        { //数字判定
            if (num[i] < '0' || '9' < num[i])
                flag = 1;
        }

        if (flag == 0)
            push(atoi(num)); //数字

        if (num[0] == '+' || num[0] == '-' || num[0] == '*')
            calc(num[0]); //演算子
    }
    printf("%d\n", s[1]);

    return 0;
}

void push(int x)
{
    s[top] = x;
    // printf("入った数字%d\n",s[top]);
    top++;
}

void calc(char ope)
{
    top--;
    if (ope == '+')
        s[top - 1] = s[top - 1] + s[top];
    if (ope == '-')
        s[top - 1] = s[top - 1] - s[top];
    if (ope == '*')
        s[top - 1] = s[top - 1] * s[top];

    // printf("")
}
