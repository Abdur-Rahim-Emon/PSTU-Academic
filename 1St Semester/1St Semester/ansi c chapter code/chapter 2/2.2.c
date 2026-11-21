#include <stdio.h>

void drawBar(int length) {
    int i, j;
    for (i = 0; i < length; i++) {
        for (j = 0; j < i; j++)
            printf(" ");
        printf("██\n");
    }
}

int main() {
    int length;
    printf("Enter the length of the bar: ");
    scanf("%d", &length);
    printf("\n");
    drawBar(length);
    return 0;
}
