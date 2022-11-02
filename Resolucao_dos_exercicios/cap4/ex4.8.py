#Escreva um programa que leia dois números e que pergunte qual
#operação você deseja realizar. Você deve poder calcular soma (+ ), subtração (-),
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada.

n1 = float(input('Digite o primeiro número: '))
print('''[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão''')
ope = int(input('Sua escolha: '))
n2 = float(input('Agora digite o segundo número: '))
if ope == 1:
    print(f'{n1} + {n2} = {n1 + n2}')
elif ope == 2:
    print(f'{n1} - {n2} = {n1 - n2}')
elif ope == 3:
    print(f'{n1} x {n2} = {n1 * n2}')
elif ope == 4:
    if n2 > 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        print('Não existe divisão para denominadores menores que zero!!!!')
else:
    print('Tentantiva inválida, tente novamente')
