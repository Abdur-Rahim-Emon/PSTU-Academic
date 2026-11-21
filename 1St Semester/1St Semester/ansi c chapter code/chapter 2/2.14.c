#include<stdio.h>
#include<math.h>
#define PI 3.1416
int main()
{
    int c=0,c1=0;
    int a=4,b=5;
    float r;
    r=sqrt((a*a*1.00)+(b*b*1.00));
    float area;
    area=PI*r*r;
    printf("Area of circle: %f",area);
    float pre;
    pre=2*PI*r;
    printf("\nPerameter: %f",pre);
}

