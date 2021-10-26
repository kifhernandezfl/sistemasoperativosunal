#include <stdio.h>
#include <stdlib.h>

int main () {
   char *str;

   str = (char *) malloc(8);
   strcpy(str, "Ejemplo");
   printf("String = %s,  Address = %u\n", str, str);

   free(str);
   
   return(0);
}