#include<stdio.h>
int main()
{
    int a[5],count=0;
    for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    for(int i=0; i<5; i++)
    {
        for(int j=i+1; j<5; j++)
        {
            if(a[i]==a[j])
                {count++;
                break;
                }
        }
    }
    printf("Total number of duplicate elements found in the array is : %d ",count);
}
