
#include<stdio.h>
int main()
{
    float p,c,d,n;
    printf("Enter the value of c,d,p: ");
    scanf("%f %f %f",&c,&d,&p);
   float x,x1;
   x=log(p/c);
   printf("x=%f\n",x);
   x1=log(1-(d*.01));
   printf("x1=%f\n",x1);
   n=x/x1;
   printf("N= %.4f\n",n);


}
