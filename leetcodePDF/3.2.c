#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main()
{
	int val;
	char str[20];

	strcpy(str, "+098");
	val = atoi(str);
	printf("字符串值 = %s, 整型值 = %d \n", str, val);

	return 0;
}