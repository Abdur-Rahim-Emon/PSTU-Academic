#include<stdio.h>
#include<math.h>
int main()
{
    float l=.99,r=0.00998,c;
    printf("enter the c vlaue within (0.01 to 0.1)=");
    scanf("%f",&c);
    float f1,f2,f;
    f1=1/(l*c);
    //printf("f1=%f\n",f1);
    f2=(r*r)/(4*c*c);
    //printf("f2=%f",f2);
    f=sqrt(f1-f2);
    printf("Frequency =%.3f",f);
}
