
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
    printf("The Second largest element in the array is : %d",a[n-2]);




}

