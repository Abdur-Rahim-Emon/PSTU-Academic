
#include<stdio.h>
int main()
{

    int n;
    printf("Input the size of array : ");
    scanf("%d",&n);
    int a[n];
     for(int i=0; i<n; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }

     printf("Input the position where to delete: ");
     int d;
     scanf("%d",&d);
     for(int i=(d-1); i<(n-1);i++)
     {
        a[i]=a[i+1];

     }
     for(int i=0; i<(n-1); i++)
     {
         printf("%d ",a[i]);
     }



}
