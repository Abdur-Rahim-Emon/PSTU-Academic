
#include<stdio.h>
int main()
{
    int a[3],b[3];
    printf("First array is: \n");
    for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    printf("Secend array is: \n");
    for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&b[i]);
    }
    int temp;
    for(int i=0; i<3; i++)
    {
        for(int j=i+1; j<3; j++)
        {
            if(a[i]<a[j])
            {
               temp=a[j];
               a[j]=a[i];
               a[i]=temp;
            }
        }
    }
     for(int i=0; i<3; i++)
    {
        for(int j=i+1; j<3; j++)
        {
            if(b[i]<b[j])
            {
                temp=b[j];
               b[j]=b[i];
               b[i]=temp;
            }
        }
    }
    printf("The merged array in decending order is : \n");
     for(int i=0; i<3; i++)
    {
        printf("%d %d ",a[i],b[i]);
    }
}
