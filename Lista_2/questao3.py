"""QUESTÃO 3 - Crie um jogo simples de adivinhação em que o programa escolhe um número aleatório entre 1 e 10 e o usuário tem que adivinhar."""

#Modulos e Métodos

import random

senha = random.sample(range(0,9),4)

while True:
    palpite = input("\nEntre com 4 dígitos: ")
    for i, num in enumerate (palpite):
        if int(num) == senha[i]:
            print (f'{num}', end='')
        elif int (num) in senha:
            print('?', end='')
        else:
            print('X', end='')   

    if [int(i) for i in palpite] == senha:
        print('\nAcertou!', palpite)
        break         