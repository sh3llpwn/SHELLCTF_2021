#include<stdio.h>
#include<string.h>
int domain_expansion(char n[])
{
	char one[50] = "SHELL{";
	char two[50] = "5hR1n3}";
	char three[50] = "M3L0v4l3nT_";
	strcat(one,three);
	strcat(one, two);
	return strcmp(n,one);
}

int main()
{
	char a[50];
	printf("Enter your flag:");
	scanf("%s",a);
	char res1[100] = "Congrats your flag is correct.";
	char res2[100] = "Better luck next time";
	if (domain_expansion(a) == 0)
	{
		printf("%s",res1);
	}
	else
	{
		printf("%s",res2);
	}
	return 0;
}
