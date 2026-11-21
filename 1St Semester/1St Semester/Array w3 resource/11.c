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
    for(int i=0; i<5; i++)
    {

        for(int j=i+1; j<5; j++)
    {
        if(a[i]>a[j])
        {
            temp=a[j];
            a[j]=a[i];
            a[i]=temp;

        }

    }

    }

        printf("Elements of array in sorted ascending order: \n");
        for(int i=0; i<5; i++)
        {
            printf("%d ",a[i]);
        }



}
