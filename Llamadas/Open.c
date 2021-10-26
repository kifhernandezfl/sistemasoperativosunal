#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv)
{
	FILE *ejemplo;
    ejemplo = fopen("ejemplo.txt", "r"); //Crea y abre el archivo ejemplo

    if (ejemplo == NULL)
    {
        perror("Error abriendo");
        exit(-1);
    }

    fclose ( ejemplo );

    return 0;
}