#include<stdio.h>
int main()
{
    int a[3];
    for(int i=0; i<3; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
    }
    int sum=0;
    for(int i=0; i<3; i++)
    {
        sum=sum+a[i];
    }
    printf("%d",sum);
}
