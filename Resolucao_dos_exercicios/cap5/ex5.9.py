'''Escreva um programa que leia dois números. Imprima a divisão
inteira do primeiro pelo segundo, assim como o resto da divisão. Utilize apenas
os operadores de soma e subtração para calcular o resultado. Lembre-se de que
podemos entender o quociente da divisão de dois números como a quantidade de
vezes que podemos retirar o divisor do dividendo. Logo, 20 .;- 4 = 5, uma vez que
podemos subtrair 4 cinco vezes de 20. '''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
resto = 0
count = n1
count_divisao = 0
subtrador = n1
while subtrador > 0:
    subtrador -= n2
    count_divisao += 1
    if subtrador < n2:
        resto = subtrador
        break
print(f'A divisão será {count_divisao} e o resto é {resto}')