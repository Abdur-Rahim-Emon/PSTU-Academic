#include<stdio.h>
int main()
{
    float c1,b1;
    printf("Enter number  of call of customer:");
    scanf("%f",&c1);
    if(c1<=100)
        b1=250;
    else
        b1=(250+c1*1.25);
    printf("Amount of call rate:%f",b1);
}
