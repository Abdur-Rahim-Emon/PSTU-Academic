
#include<stdio.h>
int main()
{

    int n;
    printf("Input the size of the square matrix (less than 5): ");
    scanf("%d",&n);
    int a[n][n],b[n][n];
    printf("Input elements in the first matrix :\n ");
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("element -[%d][%d]: ",i,j);
            scanf("%d",&a[i][j]);


        }

    }
    printf("Input elements in the secend matrix :\n ");
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("element -[%d][%d]: ",i,j);
            scanf("%d",&b[i][j]);


        }

    }
    printf("The First matrix is : \n");
    for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("%d ",a[i][j]);

        }
        printf("\n");
    }
     printf("The secend matrix is : \n");
        for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("%d ",b[i][j]);

        }
        printf("\n");
    }
    printf("The addition of two matrix is : \n");
        for(int i=0; i<n; i++)
    {
        for(int j=0; j<n; j++)
        {

            printf("%d ",a[i][j]+b[i][j]);

        }
        printf("\n");
    }




}


