//REVISÃO DE LÓGICA DE PROGRAMAÇÃO EM C - EXERCÍCIOS

/*QUESTÃO 1 - Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9.


- Lógica:

42339 = 4**10000 + 2**1000 + 3**1000 + 3**10 + 9*1
42339 | 10000 = 4
42339 % 10000 = 2339

2339/1000 = 2
2339%1000 = 339

339/100 = 3
339%100 = 39

39/10 = 3
39%10 = 9

9/1 = 9

9%1 = 0
*/

#include<stdio.h>
#include<math.h>

//contador de digitos
int main(){
	long num, div;
	int count = 0;
	
	printf("Digite o numero: ");
	scanf("%ld", &num);
	
	div = 1;
	while(num/div){
		
		count++;
		div = pow(10, count);
		
	}
	
	printf("Tem %d digitos", count);

//separando os numeros
	while(num!=0){
		printf("%ld ", num/(long)pow(10, count-1));
		num = num%(long)pow(10, count-1);
		count--;
	}
}



