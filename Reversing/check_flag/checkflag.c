#include<stdio.h>
int checkflag(int x)
{
	if(x == 2323)
	{
		printf("Congrats you got it.");
		printf("\tThis is the flag\n");
		printf("SHELL{bas1c_r3v}");
		return 0;
	}
	else
	{
		printf("sorry try again.");
		return 1;
	}
}
int main()
{
	int a;
	printf("Enter your number:");
	scanf("%d",&a);
	checkflag(a);
	int status = 1;
	while(status == 1)
	{
		int a;
		printf("\nEnter your number:");
		scanf("%d",&a);
		int ans = checkflag(a);
		if (ans == 1)
		{
			status = 1;
		}
		else
		{
			status = 0;
		}
	}
	
	return 0;
}
