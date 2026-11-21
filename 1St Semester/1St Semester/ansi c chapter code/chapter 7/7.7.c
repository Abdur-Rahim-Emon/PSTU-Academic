#include<stdio.h>
int main()
{
    float x=0;
    float y;
    printf("\n\n-----\n");
    printf("x");
    for(int i=0; i<10; i++)
    {
        for(int j=0; j<10; j++)
        {
            y=exp(-i);
            printf("%.2f",y);

        }printf("\n");
    }

}
