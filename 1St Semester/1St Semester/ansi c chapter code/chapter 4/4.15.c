#include<stdio.h>
int main()
{
    float s,r;
    for(int i=0; i<=100; i++)
    {
       s=i*i;
       r=sqrt(i);
       printf("sqaure: %.2f Root: %.2f\n",s,r);
    }
}
