#include <stdio.h>
#include <math.h>

int main() {
    int  number;


    printf("Enter a integer number: ");
    scanf("%d", &number);
     int temp;
     temp=number;
     int sum=0,rem;
    while(temp!=0)
    {
        rem=temp%10;
        sum=sum+rem;
        temp=temp/10;
    }



    printf("sum of the digit is : %d\n", sum);

    return 0;
}
