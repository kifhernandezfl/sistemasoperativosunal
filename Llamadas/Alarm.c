#include<signal.h>
#include<stdio.h>
#include<stdlib.h>
 
void manejador(int signum);
int flag = 1;
 
main(int argc, char **argv)
{
 
	signal(SIGALRM,manejador);
	printf("Alarma\n");
	alarm(10); //Crear alarma en 10 segundos


	while(flag);
 
}
 
void manejador (int signum)
{
	printf("\nRecibi una alarma\n");
	flag=0;
}