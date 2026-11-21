#include<stdio.h>
int main()
{
    int first=0,s=1,count=0,fibo,n;
    printf("Enter range: ");
    scanf("%d",&n);
    do
    {
        if(count<=1)
            fibo=count;
        else
        {
            fibo=first+s;
            first=s;
            s=fibo;
        }
        printf("%d ",fibo);
        count++;
    }while(count<n);
}
