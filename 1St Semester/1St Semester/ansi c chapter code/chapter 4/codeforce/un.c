#include <stdio.h>

// Function to calculate the sum of elements in an array recursively
int arraySum(int arr[], int size) {
    // Base case: if array size is 0, return 0
    if (size == 0) {
        return 0;
    }
    // Recursive case: return sum of current element and sum of rest of the array
    else {
        return arr[size - 1] + arraySum(arr, size - 1);
    }
}

int main() {
    int size;
    
    // Input the size of the array
    printf("Enter the size of the array: ");
    scanf("%d", &size);
    
    int arr[size];
    
    // Input elements of the array
    printf("Enter %d elements of the array:\n", size);
    for (int i = 0; i < size; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Calculate the sum of elements using recursion
    int sum = arraySum(arr, size);
    
    // Print the sum
    printf("Sum of elements in the array: %d\n", sum);

    return 0;
}
