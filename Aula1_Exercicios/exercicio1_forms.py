

#Algoritmo - Forms de usuario

nome = input("Digite seu nome:")
idade = int(input ("Digite sua idade:"))
altura = float(input("Digite sua altura:"))
peso = float(input("Digite seu peso:"))
est_civil = input("""Digite seu estado civil:
                    S - Solteiro
                    C - Casado
                    D - Divorciado
                    V - Viúvo """).upper()


imc = peso/altura**2
if imc<17:
    pimc = "Muito abaixo do peso!"
elif imc>=17 and imc<=18.5:
    pimc = "Abaixo do peso!"
elif imc>=18.5 and imc<=25:
    pimc = "Peso normal!"
elif imc>=25 and imc<=30:
    pimc = "Acima do peso!"
elif imc>=30 and imc<=35:
    pimc = "Obesidade 1!"
elif imc>=35 and imc<=40:
    pimc = "Obesidade 2!"
else:
    pimc = "Obesidade severa!"

match est_civil:
    case 'S':
        pcivil = "Solteiro"
    case 'C':
        pcivil = "Casado"
    case 'D':
        pcivil = "Divorciado"
    case 'V':
        pcivil = "Viúvo"
    case _:
        pcivil = "ESTADO CIVIL NÃO IDENTIFICADO"
        
print(f"""
          *********************************
          *    Formulário do Usuario      *
          *                               *
          *                               *
          * - Nome: {nome}                *
          * - Idade : {idade}             *
          * - IMC: {peso/altura**2}       *
          * - {pimc}                      *
          * - Estado civil: {pcivil}      *
          *********************************
          

""")
