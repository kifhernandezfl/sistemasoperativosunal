#include <stdlib.h>
#include <stdio.h>

int main(int argc, char** argv)
{
    char c[] = "ejemplo";
    char buffer[20];

	FILE *ejemplo;
    ejemplo = fopen("ejemplo.txt", "r"); //Abre ejemplo

    if (ejemplo == NULL)
    {
        perror("Error abriendo");
        exit(-1);
    }

	fwrite(c, strlen(c) + 1, 1, ejemplo);
	
    fclose (ejemplo);

    return 0;
}