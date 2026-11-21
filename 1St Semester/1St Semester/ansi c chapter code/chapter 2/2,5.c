#include<stdio.h>
int main()
{
    int d,t;
    printf("Total travalled distance:");
    scanf("%d",&d);
    printf("Time counsume for total distance:");
    scanf("%d",&t);
    float v;
    v=d*1.00/t;
    printf("velocity is: %.4f",v);
}
