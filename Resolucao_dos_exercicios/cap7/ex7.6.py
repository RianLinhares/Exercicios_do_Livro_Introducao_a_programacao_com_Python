#Escreva um programa que leia três strings. Imprima o resultado da
#substituição na primeira, dos caracteres da segunda pelos da terceira.
#1 string: AATTCGAA
#2 string: TG
#3 string: AC
#Resultado: AAAACCAA

palavra1 = str(input('Digite uma frase: ')).upper()
palavra2 = str(input('Digite uma frase: ')).upper()
palavra3 = str(input('Digite uma frase: ')).upper()
resultado = ''
for c in range(0, len(palavra2)):
    resultado = palavra1.replace(palavra2[c], palavra3[c])
print(resultado)
