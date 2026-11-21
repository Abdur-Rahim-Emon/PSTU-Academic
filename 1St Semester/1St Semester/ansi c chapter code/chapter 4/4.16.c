#include <stdio.h>

int main() {
    double distance_miles;
    int distance_kms;

    // Prompt the user to enter distance in miles
    printf("Enter distance in miles: ");
    scanf("%lf", &distance_miles);

    // Convert miles to kilometers (1 mile = 1.60934 kilometers)
    distance_kms = (int)(distance_miles * 1.60934);

    // Display the converted distance
    printf("Distance in kilometers: %d\n", distance_kms);

    return 0;
}
