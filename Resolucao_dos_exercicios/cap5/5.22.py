'''Escreva um programa que exiba uma lista de opções (menu): adição,
subtração, divisão, multiplicação e sair. Imprima a tabuada da operação escolhida.
Repita até que a opção saída seja escolhida.'''

while True:
    print('''Menu De Opções
[1] Adição
[2] Subtração
[3] Divisão
[4] Multiplicação
[5] Sair''')
    opcao = int(input('Sua Escolha: '))
    tabuada = 1
    while tabuada <= 10:
        num = 1
        if opcao == 1:
            while num <= 10:
                print(f'{tabuada} + {num} = {tabuada + num}')
                num += 1
        tabuada += 1
