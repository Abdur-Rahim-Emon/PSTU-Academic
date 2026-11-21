#include<stdio.h>
int main()
{
    float u,t,a;
    scanf("%f %f %f",&u,&t,&a);
    float s;


    s=(u*t)+ 0.5*(a*t*t);
    printf("distance= %.2f",s);

}
