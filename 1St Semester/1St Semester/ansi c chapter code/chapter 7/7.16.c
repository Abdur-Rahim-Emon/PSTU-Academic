#include <stdio.h>

int main() {
    int num, sum = 0, count = 0;

    printf("Enter 10 two-digit integers:\n");

    for (int i = 0; i < 10; i++) {
        scanf("%d", &num);

        if (num > 0) {

            if (sum + num > 999) {
                printf("Sum of positive values exceeds 999.\n");
                break;
            }


            sum += num;

            count++;
        }
    }

    printf("Sum of positive values: %d\n", sum);
    printf("Number of values added: %d\n", count);

    return 0;
}
