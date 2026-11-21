#include<stdio.h>
int main()
{
    int a[4],count=0;
    for(int i=0; i<4; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    for(int k=0; k<4; k++)
    {
        count=0;
        for(int j=(k+1); j<4; j++)
        {
            if(a[k]==a[j])
            {
                count++;

                break;
            }
        }
        if(count==0)
        printf("%d ",a[k]);



    }
}
