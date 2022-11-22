#Escreva um programa que leia duas strings e gere uma terceira com
#os caracteres comuns às duas strings lidas.
#1 string: AAACTBF
#2 string: CBT
#Resultado: CBT
#A ordem dos caracteres da string gerada não é importante, mas deve conter todas
#as letras comuns a ambas.
palavra1 = str(input('Digite uma frase: ')).upper()
palavra2 = str(input('Digite uma frase: ')).upper()
a = set(palavra1)
b = set(palavra2)
if a & b:
    comum = a & b
    print(f'Caracteres em comum: {comum}')
else:
    print('Não encontrado')