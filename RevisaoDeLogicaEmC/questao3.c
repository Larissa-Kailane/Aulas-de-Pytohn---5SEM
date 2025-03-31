
/* QUESTÃO 3 - Defina uma função recursiva para calcular a soma de dois naturais usando as funções `suc(n)` e `pred(n)` que devolvem, respectivamente, 
o sucessor e o predecessor de um natural n.

- Lógica:

3+4 = 2+5 , 1+6 = 0+7
*/

#include<stdio.h>
#include<math.h>

	int pred(int n){
		return n-1;
	}
	
	int suc(int n){
		return n+1;
	}
	
	
	int soma(int n1, int n2){
		
		if (n1==0)
		return n2;
		else
			return soma(pred(n1), suc(n2));
		
		/*while(n1 != 0){
		n1 = pred(n1);
		n2 = suc(n2);
	}
	return n2;*/
	}
	
	
	
int main(){
	int n1, n2;
	
	printf("Digite dois numeros: ");
	scanf("%d %d", &n1, &n2);
	
	
	
	printf("A soma e %d", soma(n1, n2));
}