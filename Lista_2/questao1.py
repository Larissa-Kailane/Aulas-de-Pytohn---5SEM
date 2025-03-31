
"""QUESTÃO 1 - Crie um programa que some todos os números pares entre 1 e , onde é fornecido pelo usuário."""


n = int(input("Digite um número: "))

soma = 0
for par in range(0, n+1, 2):
    soma+=par

print(f"A soma dos pares de 1 até {n} é {soma}. ")