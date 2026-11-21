#include<stdio.h>
int main()
{
        float dr,sc,hc;
        scanf("%f %f %f",&dr,&sc,&hc);
        float tbo;
        tbo=sqrt((2*sc)/(dr*hc));
        float eoq;
        eoq=sqrt((2*dr*sc)/(hc));
        printf("\nEQO =%f\nTBO =%f\n",eoq,tbo);
}
