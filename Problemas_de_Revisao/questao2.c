
/*QUESTÃO 2 - O quadrado de um número natural n é dado pela soma dos n primeiros
números ímpares consecutivos. Por exemplo,
1^2 =1, 2^2 = 1 + 3, 3^2 = 1 + 3 + 5
Dado um número n, calcule seu quadrado usando a soma de ímpares ao
invés de produto

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