#include<stdio.h>
#include<math.h>
int main()
{
    float x,x1,y,y1;
    printf("Enter the value of(x,y):");
    scanf("%f %f",&x,&y);
    printf("Enter the vlaue of (x1,y1):");
    scanf("%f %f",&x1,&y1);
    float d;
    d=sqrt((x-x1)*(x-x1)+ (y-y1)*(y-y1));
    printf("D=%.4f",d);
}
