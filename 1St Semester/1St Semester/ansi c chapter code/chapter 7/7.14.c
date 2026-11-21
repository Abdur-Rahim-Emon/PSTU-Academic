
#include<stdio.h>
int main()
{
    int x=180;
    float r;
    for(int i=15; i<=180; i=i+15)
    {
        r=sin(i);
        printf("y= sin(%d) = %.2f \n",i,r);
    }
}
