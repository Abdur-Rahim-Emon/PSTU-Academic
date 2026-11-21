#include<stdio.h>
#include<time.h>

int main()
{
    printf("system output\n");

    time_t t;
    time(&t);

    printf("current time and date (date and time): %s", ctime(&t));


    return 0;
}
