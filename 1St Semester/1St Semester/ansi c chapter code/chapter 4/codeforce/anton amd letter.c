#include<stdio.h>
#include<string.h>
int main()
{
    int n=1000;
    char ch[1000];
    int len=0;
    for(int i=0; i<n; i++)
    {
        scanf("%c",&ch[i]);

        if(ch[i]=='}')
        {
            ch[i+1]='\0';
            break;
        }
    }
    len=strlen(ch);
    int temp=len;
   // printf("%d\n",temp);
    int count=0,x=0;
    for(int i=1; i<len; i=i+3)
    {
        for(int j=i+3; j<len; j=j+3)
        {
            if(ch[i]==ch[j])
                {
                    ch[j]='1';
                }
        }
    }
    for(int i=1; i<len; i++)
    {
        x=ch[i];
        if(x>=95 && x<=122)
            count++;
    }
    printf("%d",count);
}
