#Escreva um programa que leia duas strings. Verifique se a segunda
#ocorre dentro da primeira e imprima a posição de início.
#1 string: AABBEFAATT
#2 string: BE
#Resultado: BE encontrado na posição 3 de AABBEFAATT

frase1 = str(input('Digite uma frase: ')).upper()
frase2 = str(input('Digite uma frase: ')).upper()
if frase2 in frase1:
    print(f'{frase2} encontrado na posição {frase1.find(frase2)} de {frase1}')
else:
    print(f'{frase2} não encontrada em {frase1}')
