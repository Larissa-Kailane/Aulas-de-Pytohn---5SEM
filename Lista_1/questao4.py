
"""QUESTÃO 4 - Crie um programa que peça ao usuário para digitar uma frase e conte quantas vogais (a, e, i, o, u) aparecem na frase. 
Considere que a contagem deve ser case-insensitive (ou seja, não diferencie maiúsculas de minúsculas)."""


frase = input("Entre com uma frase: ")
print(f"Na frase \"{frase}\" tem:\n",
	f"Vogal a: {frase.count("a")}\n",
	f"Vogal e: {frase.count("e")}\n",
	f"Vogal i: {frase.count("i")}\n",
	f"Vogal o: {frase.count("o")}\n",
	f"Vogal u: {frase.count("u")}\n")