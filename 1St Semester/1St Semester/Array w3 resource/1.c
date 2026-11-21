#include<stdio.h>
int main()
{
    int a[10];
     for(int i=0; i<10; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    printf("Element in array are: ");
    for(int i=0; i<10; i++)
    {

        printf("%d ",a[i]);
    }

}
