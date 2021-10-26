#include <stdio.h>
 
int main ()
{
    FILE *ejemplo = fopen("ejemplo.txt","r");
 
    if (ejemplo == NULL)
        return 0;
 
    do
    {
        char c = fgetc(ejemplo);
 
        if (feof(ejemplo))
            break ;
 
        printf("%c", c);

    }while(1);
 
    fclose(ejemplo);

    return(0);
}