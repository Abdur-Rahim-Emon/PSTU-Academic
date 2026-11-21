#include<stdio.h>
int main()
{
    int n;
    float fact=1;
    printf("enter the nth number: ");
    scanf("%d",&n);
    float e,sum=1;
    for(int i=1; i<n; i++)
    {
        fact=1;
        for(int j=1; j<=i; j++)
        {
            fact=fact*j*1.00;
        }
        sum=1/fact+sum;


    }
    printf("e=%.2f",sum);
}
