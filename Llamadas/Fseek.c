#include <stdio.h>

int main () {
   FILE *ejemplo;

   ejemplo = fopen("ejemplo.txt","w+");
   fputs("Esto es un ejemplo", ejemplo);
  
   fseek( ejemplo, 7, SEEK_SET );
   fputs(" una llamada al sistema", ejemplo);
   fclose(ejemplo);
   
   return(0);
}