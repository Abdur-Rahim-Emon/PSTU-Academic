
#include<stdio.h>
int main()
{
    for(int i=1; i<=5; i++)
    {
        for(int j=1; j<=5-i; j++)
        {
            printf(" ");
        }
        for(int k=1; k<=i; k++)
        {if(i%2!=0)
            printf("%d ",k);
            else
                printf("%c ",64+k);
        }
        printf("\n");
    }
}
