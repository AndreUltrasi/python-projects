//Script em C modificado, criado por Mohanraj do site
//http://meansofmine.blogspot.com.br/2011/04/c-program-to-implement-fcfsfirst-come.html
#include <stdlib.h>
#include <stdio.h>

//**FSFC ("First Served First Come" ou FIFO "First In First Out")**
//O primeiro elemento a ser inserido é o primeiro a ser retirado,
//é um algoritmo de escalonamento não preemptivo e que entrega a CPU os processos pela ordem de chegada
void fifo() {
	int duracao[10], espera[10];
	int qtdProcessos, i;
	float medioResposta = 0, medioEspera = 0;
	printf("**ALGORITMO DE ESCALONAMENTO FIFO**\n");
	printf("Digite o numero de processos: ");
	scanf_s("%d", &qtdProcessos);

	for (i = 0; i < qtdProcessos; i++) {
		printf("Digite o tempo de duracao do processos %d: ", i + 1);
		scanf_s("%d", &duracao[i]);
	}

	espera[0] = 0; //espera do processo 1 é sempre 0

	//Calcula o tempo de espera de cada processo
	//O tempo de resposta do anterior eh a espera do proximo
	//espera[i] eh a espera do processo i
	//espera[i + 1] eh a resposta do processo i
	for (i = 0; i < qtdProcessos; i++) {
		espera[i + 1] = espera[i] + duracao[i];
	}

	printf("\nProcessos|Duracao|Espera|Resposta\n");
	for (i = 0; i<qtdProcessos; i++) {
		printf("P[%d]\t |%d\t |%d\t|%d\n", i + 1, duracao[i], espera[i] , espera[i + 1]);
	}

	//Calcula os tempos médios 
	for (i = 0; i < qtdProcessos; i++) {
		medioEspera = medioEspera + espera[i];
		medioResposta = medioResposta + espera[i + 1];
	}
	medioEspera = medioEspera / qtdProcessos;
	medioResposta = medioResposta / qtdProcessos;

	printf("\nO tempo medio de espera eh: %.2f\n", medioEspera);
	printf("O tempo medio de resposta eh: %.2f\n\n", medioResposta);


	//gantt Chart
	printf("Gantt Chartt FIFO\n\n");
	for (i = 0; i<qtdProcessos; i++) {
		printf("[%d,%d]->P%d ", espera[i], espera[i + 1], i + 1);
	}

	printf("\n\n");
	system("pause");
	printf("\n");
}
int main() {
	while (1) { fifo(); }
}
/*
1º Executar o código com quaisquer valores
2º Mostrar como o algoritmo funciona(gantt Chart)
3º Explicar os tempos de espera, resposta e tempos médios
4º Explicar o código com o programa aberto*/