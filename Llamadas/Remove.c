#include <stdio.h>

int main () 
{
   FILE *f;
   f = fopen("ejemplo.txt", "rb+");
   fclose(f);

   remove("ejemplo.txt");
   
   return(0);
}