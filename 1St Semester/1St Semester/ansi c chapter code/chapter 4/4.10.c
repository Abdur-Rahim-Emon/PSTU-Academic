#include <stdio.h>

int main() {
    int num1, num2, num3, largest;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &num1, &num2, &num3);

    switch (num1 > num2 && num1 > num3 ? 1 : (num2 > num1 && num2 > num3 ? 2 : 3)) {
        case 1:
            largest = num1;
            break;
        case 2:
            largest = num2;
            break;
        case 3:
            largest = num3;
            break;
    }

    printf("The largest number is %d", largest);

    return 0;
}
