#include<stdio.h>
int main()
{
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d\n",x);
    printf("x\n");
    printf("%d\n",y);
    printf("-------\n");
    printf("%d\n",(x%10)*x);
    printf("%d\n",(y%10)*y);
    printf("--------------\n");
    printf("%d\n",x*y);
}
