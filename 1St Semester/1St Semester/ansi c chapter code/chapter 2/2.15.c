#include<stdio.h>
#include<math.h>
#define PI 3.1416
int main()
{
    int a=2,b=2;
    int c=5,d=6;
    float e;
    e=sqrt((a-c)*(a-c)*1.00+1.00*(b-d)*(b-d));
    float r;
    r=e/2;
    float area;
    area=PI*r*r;
    printf("Area of circle: %.4f",area);
}
