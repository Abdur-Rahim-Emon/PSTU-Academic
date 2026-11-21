
#include<stdio.h>
int main()
{

    int n=3;

    int a[n][n];
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("element -[%d][%d]: ",i,j);
            scanf("%d",&a[i][j]);


        }

    }
    printf("The matrix is : \n");
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("%d ",a[i][j]);

        }
        printf("\n");
    }




}


