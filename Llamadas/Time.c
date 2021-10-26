#include <stdio.h>
#include <time.h>
 
int main ()
{
    time_t seconds;
     
    seconds = time(NULL);
    printf("Segundos desde enero 1 de 1970 = %ld\n", seconds);
     
    return(0);
}