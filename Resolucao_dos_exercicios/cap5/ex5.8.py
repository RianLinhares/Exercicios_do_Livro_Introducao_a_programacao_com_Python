'''Escreva um programa que leia dois números. Imprima o resultado da
multiplicação do primeiro pelo segundo. Utilize apenas os operadores de soma e
subtração para calcular o resultado. Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles.
Assim, 4 x 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4. '''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
count = 1
somador = 0
while count <= n2:
    somador += n1
    print(somador)
    count += 1
print(somador)