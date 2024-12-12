#include <stdio.h>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    int choice;
    int n;
    
    printf("Enter a number (1-10): ");
    scanf("%d", &n);
    
    if (n < 1 || n > 10) {
        printf("Number out of range!\n");
        return 1;
    }
    
    printf("Choose operation:\n");
    printf("1. Factorial\n");
    printf("2. Fibonacci\n");
    scanf("%d", &choice);
    
    switch (choice) {
        case 1:
            printf("Factorial of %d is %d\n", n, factorial(n));
            break;
        case 2:
            printf("Fibonacci number at position %d is %d\n", n, fibonacci(n));
            break;
        default:
            printf("Invalid choice!\n");
            return 1;
    }
    
    return 0;
}