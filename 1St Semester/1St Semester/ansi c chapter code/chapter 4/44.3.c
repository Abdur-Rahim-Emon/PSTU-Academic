#include<stdio.h>
int main()
{
    int n;
    scanf("%d",&n);
    int temp,rem,a[10];
    temp=n;
    int j=0;
    while(temp!=0)
    {
        rem=temp%10;

        a[j]=rem;
        j++;
        temp=temp/10;
    }
    for(int i=j-1; i>=0; i--)
    {
        for(int k=i; k>=0; k--)
            printf("%d ",a[k]);
        printf("\n");
    }
}
