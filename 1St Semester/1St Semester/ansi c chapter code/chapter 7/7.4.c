#include<stdio.h>
int main()
{
    int p=1000;
    float r=0.10,v,t;
    int n;
    printf("P     R        N        V\n");
    for(int i=1; i<=10; i++)
    {
        if(r>=.10 && r<=.20)
        {
            t=pow((1+r)*1.00,i);
            v=p*(t)*1.00;

    printf("%d  %.2f   %d   %.2f\n",p,r,i,v);
             p=p+1000;
            r=r+.01;
        }
    }



}
