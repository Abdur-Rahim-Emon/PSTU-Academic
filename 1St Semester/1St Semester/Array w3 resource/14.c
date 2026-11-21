
#include<stdio.h>
int main()
{
    int a[6]={0};
    int temp;
    printf("-------------------------\n");
     for(int i=0; i<5; i++)
    {
        printf("element - %d: ",i);
        scanf("%d",&temp);
        a[i]=temp;


    }
    printf("The current list of the array :\n");
for(int i=0; i<5; i++)
        {
           printf("%d ",a[i]);
        }
    int x;
    printf("\nInput the value to be inserted : ");
    scanf("%d",&x);
     int p;
    printf("\nInput the Position, where the value to be inserted : ");
    scanf("%d",&p);
    int t;
        for(int i=5; i>=p; i--)
           a[i]=a[i-1];

           a[p-1]=x;

printf(" After Insert the element the new list is :\n");
         for(int i=0; i<6; i++)
        {
           printf("%d ",a[i]);
        }




}
