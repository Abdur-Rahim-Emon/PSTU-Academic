
#include<stdio.h>
int main()
{
    int n=12345;
    int temp=n,rem,sum=0;
    while(temp!=0)
    {
        rem=temp%10;
        sum=sum+rem;
        temp=temp/10;
    }
    printf("sum of all digit is =%d\n",sum);
}
