#include<stdio.h>
int main()
{
    int i = 0;
    FILE *ejemplo = fopen("ejemplo.txt","w");
 
    if (ejemplo == NULL)
      return 0;
 
    char string[] = "Ejemplo", received_string[20];
 
    for (i = 0; string[i]!='\0'; i++)

        fputc(string[i], fp);
 
    fclose(ejemplo);

    ejemplo = fopen("ejemplo.txt","r");
 
    fgets(received_string,20,ejemplo);
 
    printf("%s", received_string);
 
    fclose(ejemplo);

    return 0;
}