#include<stdio.h>
int main()
{
    int a[5];
    int b[5];
    for(int i=0; i<5; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&a[i]);
        b[i]=-1;
    }
    int count=1;

    for(int i=0; i<5; i++)
    {
        count=1;
        for(int j=i+1; j<5; j++)
        {
            if(a[i]==a[j])
            {
                b[j]=0;
                count++;
            }
        }
        if(b[i]!=0)
            b[i]=count;
    }
    for(int i=0; i<5; i++)
    {

            if(b[i]!=0)
   printf("%d occurs %d times\n",a[i],b[i]);






    }
}
