
#include<stdio.h>
int main()
{
    int n=12345;
    int temp=n,rem,sum=0;
    while(temp!=0)
    {
        rem=temp%10;
        sum=sum*10+rem;
        temp=temp/10;
    }
    printf("reverse number is =%d\n",sum);
}
