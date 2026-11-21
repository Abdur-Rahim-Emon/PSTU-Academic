#include<stdio.h>
int main()
{
    int d,u,i;
    printf("Enter the amount of dollar:");
    scanf("%d",&d);
    float x,y;
    x=d*0.92;
    y=d*83.02;
    printf("\nEuro:%.2f\nINR:%.2f",x,y);

}
