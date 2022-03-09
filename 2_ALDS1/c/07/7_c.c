#include <stdio.h>
#define NIL -1
#define N 10000

typedef struct data
{
    int p, l, r;
} DATA;
DATA T[N];

void Preorder(int);
void Inorder(int);
void Postorder(int);

int main()
{
    int i;
    int n;
    int id, left, right, root;
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        T[i].p = NIL;
    }

    for (i = 0; i < n; i++)
    {
        scanf("%d %d %d", &id, &left, &right);
        T[id].l = left;
        T[id].r = right;
        if (left != NIL)
            T[left].p = id;
        if (right != NIL)
            T[right].p = id;
    }

    for (i = 0; i < n; i++)
    {
        if (T[i].p == NIL)
            root = i;
    }

    printf("Preorder\n");
    Preorder(root);
    printf("\n");

    printf("Inorder\n");
    Inorder(root);
    printf("\n");

    printf("Postorder\n");
    Postorder(root);
    printf("\n");

    return 0;
}

void Preorder(int u)
{
    if (u == NIL)
        return;

    printf(" %d", u);
    Preorder(T[u].l);
    Preorder(T[u].r);
}

void Inorder(int u)
{
    if (u == NIL)
        return;

    Inorder(T[u].l);
    printf(" %d", u);
    Inorder(T[u].r);
}
void Postorder(int u)
{
    if (u == NIL)
        return;

    Postorder(T[u].l);
    Postorder(T[u].r);
    printf(" %d", u);
}
