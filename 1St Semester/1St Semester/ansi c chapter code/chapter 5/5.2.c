#include<stdio.h>
int main()
{
    float x,y;
    scanf("%f %f",&x,&y);
    float a,b,c;
    a=(x+y)/(x-y);
    b=(x+y)/2;
    c=(x*x -y*y);
    printf("Value of a:%f\n Value of b:%f\n Value of c:%f",a,b,c);

}
