#include<stdio.h>
int main()
{
    char c[]="ANIL";
    char c1[]="KUMAR";
    char c2[]="GUPTA";
    printf("%s%C.%s",c,c1[0],c2);
    printf("\n%c.%c.%s",c[0],c1[0],c2);
    printf("\n%s%c.%c",c2,c[0],c1[0]);

}
