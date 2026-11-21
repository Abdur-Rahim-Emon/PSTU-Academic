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
        if(a[i]<a[j])
        {
            temp=a[j];
            a[j]=a[i];
            a[i]=temp;

        }

    }

    }

        printf("Maximum element is =%d \n",a[4]);
        printf("Minimum element is : is =%d \n",a[0]);


}
