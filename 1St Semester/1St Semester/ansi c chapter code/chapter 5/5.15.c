#include<stdio.h>
int main()
{
    float a,r;
    int t;
    printf("Enter amount and rate of interest:");
    scanf("%f %f",&a,&r);
    printf("Time:");
    scanf("%d",&t);
    float p;
    p=(a*t*r)/100+a;
    printf("total amount after 10 year: %.4f",p);

}
