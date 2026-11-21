#include<stdio.h>
int main()
{
    int a[3];
    for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    printf("The values store into the array are :");
    for(int i=0; i<3; i++)
    {
        printf(" %d ",a[i]);
    }
    printf("\nThe values store into the array in reverse are :");
    for(int i=2; i>=0; i--)
    {
        printf("%d ",a[i]);
    }
}

