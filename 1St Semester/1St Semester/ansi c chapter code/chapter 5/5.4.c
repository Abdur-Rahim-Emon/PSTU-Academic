#include<stdio.h>'
int main()
{
    float x;
    scanf("%f",&x);
    float y=round(x);
    int a=y;
    for(int i=1; i<=a; i++)
    {for(int j=1; j<=a; j++)
        printf("* ");
        printf("\n");
    }
}
