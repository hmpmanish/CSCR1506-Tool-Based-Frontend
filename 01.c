#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *link;
};

struct node *ROOT = NULL;

void append();
void display();

int main()
{
    append();
    append();
    append();
    append();

    display();

    return 0;
}

void append()
{
    struct node *temp;
    temp = (struct node*)malloc(sizeof(struct node));

    printf("Enter the node value: ");
    scanf("%d", &temp->data);

    temp->link = NULL;

    if (ROOT == NULL)
    {
        ROOT = temp;
    }
    else
    {
        struct node *p = ROOT;

        while (p->link != NULL)
        {
            p = p->link;
        }

        p->link = temp;
    }
}

void display()
{
    struct node *p = ROOT;

    while (p != NULL)
    {
        printf("%d -> ", p->data);
        p = p->link;
    }
    printf("NULL");
}