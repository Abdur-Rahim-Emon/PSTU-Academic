#include<stdio.h>
int main()
{
    int n[100],count=0;
    for(int i=0; i<100; i++)
    {
        scanf("%d",&n[i]);
    }
    for(int i=0; i<100; i++)
    {
        if(n[i]<=60 && n[i]>=50)
            count++;
    }
    printf("the people who are above 50 to 60:%d",count);
}
