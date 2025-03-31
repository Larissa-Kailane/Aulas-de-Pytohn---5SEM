
"""QUESTÃO 5 - Uma empresa que quer enviar dados pela internet pediu-lhe que escrevesse um programa que criptografe dados a fim de que eles possam
ser transmitidos com maior segurança. Todos os dados são transmitidos como inteiros de quatro dígitos. Seu aplicativo deve ler um inteiro de quatro
dígitos inserido pelo usuário e criptografá-lo da seguinte maneira: substitua cada dígito pelo resultado da adição de 7 ao dígito, obtendo o restante
depois da divisão do novo valor por 10. Troque então o primeiro dígito pelo terceiro e o segundo dígito pelo quarto. Então, imprima o inteiro
criptografado. Escreva um aplicativo separado que receba a entrada de um inteiro de quatro dígitos criptografado e o descriptografe (revertendo o
esquema de criptografia) para formar o número original."""

#criptografia

msg = ("Digite a mensagem: ")
dig1 = (int(msg[0])+7)%10
dig2 = (int(msg[1])+7)%10
dig3 = (int(msg[2])+7)%10
dig4 = (int(msg[3])+7)%10

dig1, dig2, dig3, dig4 = dig3, dig4, dig1, dig2

print("Mensagem criptografada: {dig1, dig2, dig3, dig4}")

msg = ("Digite a mensagem: ")
dig1 = (int(msg[0])+3)%10
dig2 = (int(msg[1])+3)%10
dig3 = (int(msg[2])+3)%10
dig4 = (int(msg[3])+3)%10

print("Mensagem descriptografada: {dig1, dig2, dig3, dig4}")