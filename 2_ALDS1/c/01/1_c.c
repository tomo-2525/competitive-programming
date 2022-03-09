#include <stdio.h>
#include <math.h>

int prime_judge(int);

int main()
{

    int i, j, n, num, flag = 0;
    double tmp;
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &num);
        if (prime_judge(num) == 1)
            flag += 1;
    }

    printf("%d\n", flag);
    return 0;
}

int prime_judge(int num)
{
    int j;
    if (num == 2)
        return 1;

    if (num < 2 || num % 2 == 0)
        return 0;

    j = 3;

    while (j <= sqrt(num))
    {
        if (num % j == 0)
            return 0;
        j += 2;
    }
    return 1;
}
