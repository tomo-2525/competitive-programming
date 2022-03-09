#include <stdio.h>
#include <math.h>

typedef struct node
{
    double x, y;
} POINT;

void kock(int, POINT, POINT);

int main()
{

    int n;
    POINT p1 = {0, 0}, p2 = {100, 0};
    scanf("%d", &n);

    printf("%.8f %.8f\n", p1.x, p1.y);
    kock(n, p1, p2);
    printf("%.8f %.8f\n", p2.x, p2.y);
    printf("\n");
    return 0;
}
void kock(int n, POINT p1, POINT p2)
{

    POINT s, t, u;
    if (n == 0)
        return;

    double th = 60 * M_PI / 180;

    //p1,p2からs,t,u を計算する
    s.x = (2 * p1.x + 1 * p2.x) / 3;
    s.y = (2 * p1.y + 1 * p2.y) / 3;
    t.x = (1 * p1.x + 2 * p2.x) / 3;
    t.y = (1 * p1.y + 2 * p2.y) / 3;
    u.x = (t.x - s.x) * cos(th) - (t.y - s.y) * sin(th) + s.x;
    u.y = (t.x - s.x) * sin(th) + (t.y - s.y) * cos(th) + s.y;

    kock(n - 1, p1, s);
    printf("%.8f %.8f\n", s.x, s.y); //s

    kock(n - 1, s, u);
    printf("%.8f %.8f\n", u.x, u.y); //u

    kock(n - 1, u, t);
    printf("%.8f %.8f\n", t.x, t.y); //t

    kock(n - 1, t, p2);
}
