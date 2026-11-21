
#include<stdio.h>
int main()
{
    int x,y,z;
    scanf("%d %d %d",&x,&y,&z);
    int sum=x+z+y;
    printf("sum=%d\n",sum);
    float avg=sum/3*1.00;
    printf("average=%f\n",avg);
    if(x>y && x>z)
        printf("maximum number is: %d\n",x);
     else if(y>x && y>z)
        printf("maximum number is: %d\n",y);
    else
        printf("maximum number is: %d\n",z);
    if(x<y && x<z)
        printf("minimum number is: %d\n",x);
    else if(y<x && y<z)
        printf("minimum number is: %d\n",y);
    else
        printf("minimum number is: %d\n",z);


}
