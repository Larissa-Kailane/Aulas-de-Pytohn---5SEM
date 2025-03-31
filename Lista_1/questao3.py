
"""QUESTÃO 3 - Faça um programa que calcule a distância entre dois pontos no plano cartesiano."""


print ("Digite os valores de P1(x1, y1) e P2(x2, y2): ")
x1 = float (input("x1: "))
x2 = float (input("x2: "))
y1 = float (input("y1: "))
y2 = float (input("y2: "))


dist = ((x1-x2)**2 + (y1-y2)**2)**(1/2)
print(f"A distância entre os pontos"
f"P1 ({x1:.2f}, {y1:.2f} e P2 {x2:.2f}, {y2:.2f}) é"
f "{dist}")