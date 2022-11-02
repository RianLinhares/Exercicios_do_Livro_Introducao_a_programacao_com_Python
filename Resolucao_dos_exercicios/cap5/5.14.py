'''Escreva um programa que leia números inteiros do teclado. O pro-
grama deve ler os números até que o usuário digite O (zero). l o final da execução,
exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''
count = 0
soma = 0
while True:
    n = float(input('Digite um número a somar ou 0 para sair: '))
    if n == 0:
        break
    soma += n
    count += 1
print(f'A soma dos números digitados é igual {soma}')
print(f'Ao todo foram digitados {count} números ')
print(f'A média aritimética dos números digitados é {soma / count}')
