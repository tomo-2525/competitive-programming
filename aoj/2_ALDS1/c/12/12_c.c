#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
/*#include <math.h>*/
#include <string.h>

#define N 10005
#define INF 12345678
#define WHITE 0
#define GRAY 1
#define BLACK 2
#define NIL -1

void create_generate_super_makeone_node(int, int, int);

struct node
{
    struct node *next;
    // struct node *prev;
    int vertex;
    int omosa;
};

typedef struct node *NodePointer;
NodePointer nil;

NodePointer data[N];
//int adj[N][N];
int d[N];
int color[N];
//int check[N];
int pi[N];
//int n;
/*
  void MinHeapify(int );
  void BuildMinHeap(void );
  int  ExtractMin(void );
  void HeapDecreace(int, int );
  void dijkstra(int );
*/

int main()
{
    int ex;
    int i, j;
    int n, u, k, vertex, c;
    int uid;
    int mincost;
    int r;

    for (i = 0; i < 10001; i++)
    {
        data[i] = (NodePointer)malloc(sizeof(struct node));
        data[i]->vertex = INF;
        data[i]->omosa = INF;
        data[i]->next = NULL;
        // d[i] = INF;
        // color[i] = WHITE;
        // pi[i] = NIL;
    }

    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        d[i] = INF;
        color[i] = WHITE;
        pi[i] = NIL;

        scanf("%d%d", &uid, &k);
        r = uid;
        for (j = 0; j < k; j++)
        {
            scanf("%d%d", &vertex, &c);
            create_generate_super_makeone_node(r, vertex, c);
        }
    }

    d[0] = 0;
    for (ex = 0;; ex++)
    {
        mincost = INF;
        for (j = 0; j < n; j++)
        {
            if (color[j] != BLACK && d[j] < mincost)
            {
                mincost = d[j];
                u = j;
            }
        }

        if (mincost == INF)
            break;

        color[u] = BLACK;

        nil = data[u]->next;

        while (nil != NULL)
        {
            // if(nil != NULL) break;

            if (color[nil->vertex] != BLACK && d[u] + nil->omosa < d[nil->vertex])
            {
                //	printf("aiueo\n\n");
                pi[nil->vertex] = u;
                d[nil->vertex] = nil->omosa + d[u];
            }
            //if(nil != NULL) break;
            nil = nil->next;
            // if(nil != NULL) break;
        }
    }
    for (i = 0; i < n; i++)
    {
        printf("%d %d\n", i, d[i]);
    }

    return 0;
}

void create_generate_super_makeone_node(int r, int vertex, int c)
{
    NodePointer n;
    n = (NodePointer)malloc(sizeof(struct node));
    n->vertex = vertex;
    n->omosa = c;
    n->next = data[r]->next;
    data[r]->next = n;
}
