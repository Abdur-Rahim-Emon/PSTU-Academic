
#include<stdio.h>
int main()
{
    int a[6]={0};
    printf("-------------------------\n");
     for(int i=0; i<5; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);


    }

    int x;
    printf("Input the value to be inserted : ");
    scanf("%d",&x);

        printf("The exist array list is : \n");
        for(int i=0; i<5; i++)
        {
            printf("%d ",a[i]);
        }
         printf("\nAfter Insert the list is : \n");
         a[5]=x;
         int temp;
    for(int i=0; i<6; i++)
    {

        for(int j=i+1; j<6; j++)
    {
        if(a[i]>a[j])
        {
            temp=a[j];
            a[j]=a[i];
            a[i]=temp;

        }

    }}

         for(int i=0; i<6; i++)
        {
            printf("%d ",a[i]);
        }



}
