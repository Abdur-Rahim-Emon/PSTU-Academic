#include <stdio.h>
#include <math.h>

int main() {
    float number;


    printf("Enter a floating-point number: ");
    scanf("%f", &number);


    int right = (int)number;


     right = right % 10;


    printf("The right-most digit of the integral part is: %d\n", right);

    return 0;
}
