#include<stdio.h>
int main()
{
    for(int row=1; row<=4; row++)
    {
        for(int col=row; col>=1; col--)
        {
            printf("%d ",col%2);
        }printf("\n");
    }
}
