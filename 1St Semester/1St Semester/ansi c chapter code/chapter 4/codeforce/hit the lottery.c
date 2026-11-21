#include<stdio.h>
int main()
{

   int n;
   scanf("%d",&n);
   int a=0,b=0,c=0,d=0,e=0,f=0,temp;
   temp=n;

    a=temp/100;
    b=(temp%100)/20;
    c=((temp%100)%20)/10;
    d=(((temp%100)%20)%10)/5;
    e=((((temp%100)%20)%10)%5);
    printf("%d",a+b+c+d+e);


 

    
}