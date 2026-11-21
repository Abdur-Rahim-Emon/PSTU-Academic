#include<stdio.h>
int main()
{
    int a[3];
    int b[3];
     for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    printf("The elements stored in the first array are :\n");

    for(int i=0; i<3; i++)
    {
        printf("%d ",a[i]);
        b[i]=a[i];

    }
    printf("\n");
    printf("The elements copied into the second array are :\n");
      for(int i=0; i<3; i++)
    {
        printf("%d ",b[i]);


    }
}
