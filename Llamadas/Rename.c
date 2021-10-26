#include <stdio.h>

int main () 
{
   FILE *f;
   f = fopen("ejemplo.txt", "rb+");
   fclose(f);

   rename("ejemplo.txt", "ejemplo1.txt");
   
   return(0);
}