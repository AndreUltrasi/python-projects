//Script em C modificado, criado pelo site
//http://program-aaag.rhcloud.com/c-program-for-round-robin-scheduling/
#include <stdio.h>
#include <stdlib.h>
///Variaveis da Tabela de Execucao
int ganttP[50], ganttStartTime[50], ganttRemaining[50];

/*
o flag indica se o processos terminou ou nao. Quando o atual processo executando
acaba no atual quantum, flag vira 1. Então no final ele eh checado se flag eh 1 ou 0,
se eh 0, isso significa que o processo terah que rodar mais ciclos, caso flag for 1, isso
significa que o processo terminou e ele eh mostrado no console.*/
void roundRobin() {
	int i, qtdProcessos, tempo, restante, flag, quantum, espera = 0, resposta = 0, j = 0;
	int duracao[10], execucao[10];

	printf("**ALGORITMO DE ESCALONAMENTO ROUND ROBIN**\n");
	printf("Digite o total de processos: ");
	scanf_s("%d", &qtdProcessos);
	restante = qtdProcessos;

	for (i = 0; i < qtdProcessos; i++) {
		printf("Digite o tempo de duracao do processo %d: ", i + 1);
		scanf_s("%d", &duracao[i]);
		execucao[i] = duracao[i];
	}
	//execucao[i] eh usado para definir o tempo de execucao faltante de cada processo

	printf("Digite o quantum de tempo: ");
	scanf_s("%d", &quantum);

	printf("\n\nProcesso|Tempo de Espera|Tempo de Resposta\n");

	//O loop começa com tempo = 0, e o primeiro processa a rodar eh decidido
	//pela variavel i que inicia como 0, e flag = 0 indica que nenhum processo terminou
	for (tempo = 0, i = 0, flag = 0; restante != 0;) {

		/*É checado se o processo tem tempo restante menor que o quantum.
		Se sim, então o tempo eh incrementado e o flag eh definido para 1, o que mostra que o atual
		processo executando ja foi completado, e o execucao[i] eh definido para 0 para dizer que não resta
		mais tempo a ser executado do mesmo processo. 
		execucao[i] > 0 é necessário pra saber o processo aindapossui algo a ser executado*/
		if (execucao[i] <= quantum && execucao[i] > 0) {
			tempo += execucao[i];
			execucao[i] = 0;
			flag = 1;


			///Tabela de Execucao
			ganttP[j] = i + 1;
			ganttRemaining[j] = 0;
			ganttStartTime[j++] = tempo;

		}

		/*Se o processo tem tempo restante maior que o quantum, então apenas o tempo eh aumentado
		pelo quantum. E do execucao[i] eh retirado um quantum, ou seja, o processo executou por um quantum de tempo mais
		ainda não acabou (eh preciso checar se eh maior que 0 para não cair do if para o else if)
		execucao[i] > 0 é necessário pra saber o processo ainda possui algo a ser executado*/
		else if (execucao[i] > quantum) {
			execucao[i] -= quantum;
			tempo += quantum;


			///Tabela de Execucao
			ganttP[j] = i + 1;
			ganttRemaining[j] = execucao[i];
			ganttStartTime[j++] = tempo;
		}

		/*É checado se o processo ja acabou ou se ja foi completado antes.Se ja foi
		completado, então seus tempo de espera e de resposta são mostrados*/
		if (execucao[i] == 0 && flag == 1) {

			//restante se refere a quantidade restante de processos
			restante--;

			//Processo, Tempo de Espera e Tempo de Resposta
			printf("P[%d]\t|\t%d\t|\t%d\n", i + 1, tempo - duracao[i], tempo);
			espera += tempo - duracao[i];
			resposta += tempo;
			flag = 0;
		}

		/*Checa se o contador de processos chegou ao fim. Se sim, então o contador eh definido denovo para 0 
		, e então, o loop eh reiniciado(para voltar a checar se os processos ja acabaram seu tempo de execução).
		Se o contador nao chegou ao fim, eh apenas incrementado em 1 (assim passa para o processo seguinte).*/
		if (i == qtdProcessos - 1)
			i = 0;
		else
			i++;
	}
	float medioEspera = espera;
	float medioResposta = resposta;
	printf("\nTempo medio de espera = %.2f\n", medioEspera / qtdProcessos);
	printf("Tempo medio de resposta = %.2f\n", medioResposta / qtdProcessos);
	printf("\n");

	///Tabela de Execucao
	printf("Gantt Chart RoundRobin\n\n");
	for (i = 0; i<j; i++) {
		printf("[%d,%d,%d]->P%d ", ganttStartTime[i - 1], ganttStartTime[i], ganttRemaining[i], ganttP[i]);
	}
	printf("\n\n");
	system("pause");
	printf("\n");
}
int main() {
	while (1) { roundRobin(); }
}