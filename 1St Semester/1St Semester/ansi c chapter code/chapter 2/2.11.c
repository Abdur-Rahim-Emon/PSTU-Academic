#include<stdio.h>
#include<math.h>
int main()
{
    float s,a,b,c;
    printf("Input the value of a,b,c:");
    scanf("%f %f %f",&a,&b,&c);
    s=(a+b+c)/2;
    printf("s=%f\n",s);
    float r,r1;
    r=s*(s-a)*(s-b)*(s-c);

    r1=sqrt(r);
    printf("ARea of traingle: %.4f",r1);
    return 0;
}
