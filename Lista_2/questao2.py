"""QUESTÃO 2 - Escreva um aplicativo que solicita ao usuário que insira o tamanho do lado de um quadrado e, então, exibe um quadrado vazio 
desse tamanho com asteriscos. Seu programa deve trabalhar com quadrados de todos os comprimentos de lado possíveis entre 1 e 20."""


lado = int(input("Digite o lado do quadrado: "))

print("*"*lado)
for i  in range(lado - 2):
	print("*"+" "*lado+" ")
print("* "*lado)
	