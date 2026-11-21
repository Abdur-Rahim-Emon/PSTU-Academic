#include<stdio.h>
#include<time.h>

int main()
{
    printf("System time \n");

    time_t t;
    time(&t);

    printf("\nSystem current  (date and time): %s", ctime(&t));

    return 0;
}

