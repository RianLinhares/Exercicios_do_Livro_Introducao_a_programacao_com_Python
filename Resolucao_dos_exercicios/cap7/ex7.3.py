#Escreva um programa que leia duas strings e gere uma terceira apenas
# com os caracteres que aparecem em uma delas.
#1 string: CTA
#2 string: ABC
#3 string: BT
#A ordem dos caracteres da terceira string não é importante.
palavra1 = str(input('Digite uma frase: ')).upper()
palavra2 = str(input('Digite uma frase: ')).upper()
a = set(palavra1)
b = set(palavra2)
palavra3 = ''
if a ^ b:
    incomum = a ^ b
    for c in incomum:
        palavra3 += c
    print(f'Caracteres incomuns: {palavra3}')
else:
    print(f'Não existe caracteres incomuns!!')
