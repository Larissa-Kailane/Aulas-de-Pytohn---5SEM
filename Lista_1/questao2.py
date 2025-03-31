
"""QUESTÃO 2 - Escreva um aplicativo que insere um número consistindo em cinco dígitos do usuário, separa o número em seus dígitos individuais e imprime os
dígitos separados uns dos outros por três espaços cada. Por exemplo, se o usuário digitar o número 42339, o programa deve imprimir: 4 2 3 3 9."""

           
num =  input ("Digite um número: ")
i = 0
while i<len(num):
		print (num[1], end=" ")
		i+=1
