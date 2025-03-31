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
*/


/*QUESTÃO 2 - O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares consecutivos. Por exemplo, 1^2 =1, 2^2 = 1 + 3, 3^2 = 1 + 3 + 5
Dado um número n, calcule seu quadrado usando a soma de ímpares ao invés de produto

- Lógica:

posições…

0 1 2 3 4 5  6  7  8  9
1,3,5,7,9,11,13,15,17,19...
1 = 1+2**0 - posição
3 = 1+2 = 1+2**1
5 = 1+2+2 = 1+2**2
7 = 1+2+2+2 = 1+2**3

4^2 = 16

4 = 1+3+5+7 = 16


*/

#include<stdio.h>
#include<math.h>


int main(){
	int num, soma=0;
	
	printf("Digite um numero: ");
	scanf("%d", &num);
	
	for(int i=1; i<=num; i++){
		 soma += (i*2)+1;
	}
	
	printf("%d^2=%d", num, soma);
}