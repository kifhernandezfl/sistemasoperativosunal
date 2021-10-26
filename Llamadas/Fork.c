#include <stdio.h>
#include <unistd.h>

int main(void)
{
    fork(); // En este punto el programa crea un clon de si mismo

    printf("Hola mundo, mi PID es: %d\n", getpid());
}