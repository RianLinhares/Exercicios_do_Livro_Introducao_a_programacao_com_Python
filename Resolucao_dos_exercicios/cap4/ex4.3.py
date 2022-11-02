#Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))

if n1 > n2 and n1 > n3:
    print(f'O maior é Primeiro número!')
if n2 > n1 and n2 > n3:
    print(f'O maior é Segundo número!')
if n3 > n2 and n3 > n1:
    print(f'O maior é Terceiro número!')
