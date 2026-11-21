
#include<stdio.h>
int main()
{
    int a[5];
     for(int i=0; i<5; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);

    }
   int temp;
     printf("The Even elements are : \n");
    for(int i=0; i<5; i++)
    {
        if(a[i]%2!=0)
            printf("%d ",a[i]);

    }
     printf("\nThe Odd elements are :\n");
    for(int i=0; i<5; i++)
    {
        if(a[i]%2==0)
            printf("%d ",a[i]);

    }





}
